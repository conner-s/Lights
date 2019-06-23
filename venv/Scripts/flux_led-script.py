#!C:\Users\conne\PycharmProjects\Lights\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flux-led==0.22','console_scripts','flux_led'
__requires__ = 'flux-led==0.22'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flux-led==0.22', 'console_scripts', 'flux_led')()
    )
