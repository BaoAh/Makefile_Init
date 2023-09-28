import os
import sys
import file_processing as fp
import config as cf
from argparse import ArgumentParser
import gen_make

def check_n_mkdir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"Directory '{dir_path}' created.")

def init_dir(settings):
    root_dir=settings["root_dir"]
    check_n_mkdir(root_dir)
    src_name=settings["src_dir"]
    script_name=settings["script_dir"]
    inc_name=settings["inc_dir"]
    build_name=settings["build_dir"]
    docs_name=settings["docs_dir"]
    # print(settings)
    src_ex,src_dir = fp.check_directory_existence(root_dir,src_name)
    script_ex,script_dir = fp.check_directory_existence(root_dir,script_name)
    include_ex,include_dir = fp.check_directory_existence(root_dir,inc_name)
    build_ex,build_dir = fp.check_directory_existence(root_dir,build_name)
    docs_ex,docs_dir = fp.check_directory_existence(root_dir,docs_name)
    if not src_ex:
        src_dir = os.path.join(root_dir, src_dir)
        os.makedirs(src_dir)  
        print("create src directory")
    if not include_ex:
        include_dir = os.path.join(root_dir,include_dir)
        os.makedirs(include_dir)
        print("create include directory")
    if not build_ex:
        build_dir = os.path.join(root_dir, build_dir)
        os.makedirs(build_dir)
        print("create build directory")
    if not script_ex:
        script_dir = os.path.join(root_dir, script_dir)
        os.makedirs(script_dir)    
        print("create script directory")
    if not docs_ex:
        docs_dir = os.path.join(root_dir, docs_dir)
        os.makedirs(docs_dir)
        print("create docs directory")
        

def args_parser():
    parser = ArgumentParser(prog="Project generator",usage="Initialize a project for C/C++, verilog and python")
    parser.add_argument("-c","--c_project",dest="c_project",action="store_true",help="create a new C project")
    parser.add_argument("-C","--cpp_project",dest="cpp_project",action="store_true",help="create a new C++ project")
    parser.add_argument("-v","--verilog_project",dest="verilog_project",action="store_true",help="create a new verilog project")
    parser.add_argument("-p","--python_project",dest="python_project",action="store_true",help="create a new python project")
    parser.add_argument("-f", "--flags", dest="flags", help="flags for the compiler and typed within quotes", default="")
    parser.add_argument("-o", "--output-target", dest="target", help="output file name from compiler. Default: a.out", default="a.out")
    parser.add_argument("-s", "--custom-setting", dest="cs",action="store_true", help="customize your file structure using json")
    parser.add_argument("-r", "--rearrange file", dest="ra",action="store_true", help="rearrange file")
    args = parser.parse_args()
    return args,parser


def project_init():
    args,parser = args_parser()
    
    if len(sys.argv) <= 1:
        parser.print_help()
    else:
        init_dir(cf.conf)
        if args.c_project:
            print("Initializing a C project...")
            makefile_content = gen_make.gen_file_CCpp(args) 
        elif args.cpp_project:
            print("Initializing a C++ project...")
            makefile_content = gen_make.gen_file_CCpp(args) 
        elif args.verilog_project:
            print("Initializing a verilog project...")
            makefile_content = gen_make.gen_file_verilog(args) 
        elif args.python_project:
            print("Initializing a python project...")
        
        with open(os.path.join(cf.conf["root_dir"],"Makefile"), "w") as makefile:
            makefile.write(makefile_content)
            print("writing Makefile...")
        print("create successfully")
        os.system('tree {}'.format(cf.conf["root_dir"]))
        

if __name__ == "__main__":
    project_init()