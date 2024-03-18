import argparse
def main():
    banner()
    parser = argparse.ArgumentParser(description="这是脚本的提示信息")
    parser.add_argument('-u','--url',type=str,help='请输入你的url')
    parser.add_argument('-f','--file',type=str,help='请输入文件名')
    args = parser.parse_args()
    print(args.url)
def banner():
    banner = """
,,                  ,,                
||           '      ||      _         
||/\\  _-_  \\  _-_ ||/\\  < \,  /'\\ 
|| || || \\ || ||   || ||  /-|| || || 
|| || ||/   || ||   || || (( || || || 
\\ |/ \\,/  \\ \\,/ \\ |/  \/\\ \\,/  
  _/                  _/              
"""
    print(banner)
if __name__ == '__main__':
    main()