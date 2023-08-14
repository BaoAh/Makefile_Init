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
    inc_name=settings["inc_dir"]
    build_name=settings["build_dir"]
    docs_name=settings["docs_dir"]
    # print(settings)
    src_ex,src_dir = fp.check_directory_existence(root_dir,src_name)
    include_ex,include_dir = fp.check_directory_existence(root_dir,inc_name)
    build_ex,build_dir = fp.check_directory_existence(root_dir,build_name)
    docs_ex,docs_dir = fp.check_directory_existence(root_dir,docs_name)
    if not src_ex:
        src_dir = os.path.join(root_dir, src_dir)
        os.makedirs(src_dir)    
    if not include_ex:
        include_dir = os.path.join(root_dir,include_dir)
        os.makedirs(include_dir)
    if not build_ex:
        build_dir = os.path.join(root_dir, build_dir)
        os.makedirs(build_dir)
    if not docs_ex:
        docs_dir = os.path.join(root_dir, docs_dir)
        os.makedirs(docs_dir)
        

def args_parser():
    parser = ArgumentParser(prog="Project generator",usage="Initialize a project for C/C++, verilog and python")
    parser.add_argument("-c","--c_project",dest="c_project",action="store_true",help="create a new C project")
    parser.add_argument("-C","--cpp_project",dest="cpp_project",action="store_true",help="create a new C++ project")
    parser.add_argument("-v","--verilog_project",dest="verilog_project",action="store_true",help="create a new verilog project")
    parser.add_argument("-p","--python_project",dest="python_project",action="store_true",help="create a new python project")
    parser.add_argument("-f", "--flags", dest="flags", help="flags for the compiler and typed within quotes", default="")
    parser.add_argument("-o", "--output-target", dest="target", help="output file name from compiler. Default: a.out", default="a.out")
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
        
        with open(os.path.join(cf.conf["root_dir"],"Makefile_tmp"), "w") as makefile:
            makefile.write(makefile_content)


if __name__ == "__main__":
    project_init()