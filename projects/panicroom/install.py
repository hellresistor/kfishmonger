import sys, os, shutil, inspect;

CURRENTDIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())));
ROOT = os.path.dirname(CURRENTDIR);
sys.path.append(ROOT);

from api.apt import Apt;
from api.systemctl import Systemctl;
from api.pip import Pip;
from api.log import Log;
from api.config_project import ConfigProject
from api.CONST import *;

log = Log("panicroom");
# =========== INSTALAÇÃO DE DEPENDENCIAS ==================


# =========== COPIA DE RESOURCES ==========================
config_project = ConfigProject("panicroom", log=log);
config_project.copy();
config_project.execute = True;
config_project.save();

shutil.copy( CURRENTDIR + "/resources/" + PANICROOM_SERVICE, "/etc/systemd/system/");

# =========== INICIANDO SERVICOS E PROGRMAS ===============
ctl = Systemctl( PANICROOM_SERVICE , log=log);
ctl.reload();
ctl.start();
ctl.enable();
if ctl.status():
    print("Rodando");
else:
    print("Nao está rodando.");