import sys
import config as cf

def gen_file_CCpp(args):
    content = "# makeinit was written by BaoAh \n\n"
    # Compiler specific variables
    if args.c_project:
        content += "COMPILER  := gcc\n"
        content += "SRCEXT    := c\n"
    elif args.cpp_project:
        content += "COMPILER  := g++\n"
        content += "SRCEXT    := cpp\n"
    content += "FLAGS     := " + args.flags + "\n"

    content += "SRC_DIR   := " + cf.conf["src_dir"] + "\n"
    content += "INC_DIR   := " + cf.conf["inc_dir"] + "\n"
    content += "BUILD_DIR := " + cf.conf["build_dir"] + "\n"
    content += "TARGET    := " + args.target + "\n"
    content += "SOURCES   := $(wildcard $(SRC_DIR)/*.$(SRCEXT))\n"
    content += "OBJECTS   := $(patsubst $(SRC_DIR)/%.o,$(BUILD_DIR)/%.o,$(SOURCES:.$(SRCEXT)=.o))\n"
    content += "\n\nall: $(TARGET)\n\n"
     # Main compilation
    content += "$(TARGET): " + ("$(OBJECTS)\n")
    content += "\t$(COMPILER) " + ("") + "-o $(TARGET) " + ("$^") + "\n\n"
    # Object files
    content += "$(BUILD_DIR)/%.o: $(SRC_DIR)/%.$(SRCEXT)\n"
    content +="\t$(COMPILER) $< $(FLAGS) -c -o $@\n"
    ## Clean
    content += "\n"
    content += "clean:" + "\n"
    content += "\t" + "-rm $(TARGET) " + ("$(OBJECTS)") + "\n"
    ## Run
    content += "\n"
    content += "run: all\n"
    content += "\t./$(TARGET)\n"

    return content

def gen_file_verilog(args):
    content = "# makeinit was written by BaoAh \n\n"
    # Compiler specific variables
    content += "ROOT_DIR   := $(PWD)\n"
    content += "BUILD      := " + cf.conf["build_dir"] + "\n"
    content += "BUILD_DIR  := $(ROOT_DIR)/$(BUILD)"  + "\n"
    content += "SRC_DIR    := " + cf.conf["src_dir"] + "\n"
    content += "SIM_DIR    := $(ROOT_DIR)/sim"  + "\n"
    content += "SYN_DIR    := $(ROOT_DIR)/syn"  + "\n"
    content += "SCRIPT_DIR := $(ROOT_DIR)/script"  + "\n"
    content += "REPORT_DIR := $(ROOT_DIR)/report"  + "\n\n"
    content += "TOP        := " + cf.conf["top"] + "\n"
    content += "TB_TOP     := " + cf.conf["tb_top"] + "\n"
    
    # Create folders
    content += "\n"
    content +="init: clean\n"
    content += "\tmkdir -p $(BUILD_DIR) $(SYN_DIR) $(REPORT_DIR)\n"
    # RTL
    content += "\n"
    content += "rtl: $(BUILD)\n"
    content += "\tcd $(BUILD_DIR); \\\n"
    content += "\tncverilog $(SIM_DIR)/$(TB_TOP).v $(SRC)\\\n"
    content += "\t+incdir+$(SRC_DIR) \\\n"
    content += "\t+nc64bit \\\n"
    content += "\t+access+r \\\n"
    content += "\t+define+FSDB_FILE=\"$(TOP).fsdb\" \n"

    # Syn directory init
    content += "\n"
    content += "syn_init:\n"
    content += "\tmkdir -p $(SYN_DIR)\n";

    content += "\n"
    content += "syn: $(BUILD) syn_init\n"
    content += "\tcd $(BUILD_DIR); \\\n"
    content += "\tncverilog $(SIM_DIR)/$(TB_TOP).v $(SYN_DIR)/$(TOP)_syn.v \\\n"
    content += "\t-v $(CBDK_DIR)/$(CORE_CELL) \\\n"
    content += "\t+incdir+$(SRC_DIR) \\\n"
    content += "\t+nc64bit \\\n"
    content += "\t+access+r \\\n"
    content += "\t+define+FSDB_FILE=\"$(TOP).fsdb\" \\\n"
    content += "\t+define+SDF \\\n"
    content += "\t+define+SDFFILE=\"$(SYN_DIR)/$(TOP)_syn.sdf\" \n"

    return content