from datetime import datetime
try:
    from colorama import Fore, Style, init as color_init
    color_init(autoreset=True)
except Exception:
    class C: GREEN=''; MAGENTA=''; CYAN=''; RESET_ALL=''
    Fore = C(); Style = C()
def log_header(title):
    sep = '='*len(title)
    print('\n' + Fore.CYAN + sep)
    print(Fore.CYAN + title)
    print(Fore.CYAN + sep + Style.RESET_ALL + '\n')
def log_section(name):
    print('\n' + Fore.MAGENTA + '---- ' + name + ' ----' + Style.RESET_ALL)
def log_line(text):
    ts = datetime.now().strftime('%H:%M:%S')
    print(Fore.GREEN + f'[{ts}] ' + text + Style.RESET_ALL)
