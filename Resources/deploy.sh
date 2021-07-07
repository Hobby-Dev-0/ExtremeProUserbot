
# Ultroid - UserBot
# Copyright (C) 2020 ULTROID-OP
#
# This file is a part of < https://github.com/ULTROID-OP/ULTROID-BOT/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ULTROID-OP/Ultroid/blob/main/LICENSE/>.

echo "
	      ╔╦╦╦══╦═╦═╦══╦══╗
	      ║║║╠╗╔╣╬║║╠║║╩╗╗║
	      ║║║╚╣║║╗╣║╠║║╦╩╝║
	      ╚═╩═╩╝╚╩╩═╩══╩══╝
	    °•° Deployment Begins •°•
"
echo '
        •• Getting Packages and Installing
'

export DEBIAN_FRONTEND=noninteractive
export TZ=Asia/Kolkata
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

apt-get update
apt-get upgrade -y
apt-get install -y --no-install-recommends ffmpeg neofetch mediainfo megatools
apt-get autoremove --purge

echo '
        •• Cloning Repository
'
git clone https://github.com/amanpandey7647/ExtremeProUserbot.git /root/amanpandey7647/

echo '
	•• Getting Libraries and Installing
'
pip install --upgrade pip setuptools wheel
pip install search-engine-parser
pip install -r /root/amanpandey7647/requirements.txt

echo "
			      ┏┳┓╋┏┓╋╋╋╋┏┓┏┓
			      ┃┃┣┓┃┗┳┳┳━╋╋┛┃
			      ┃┃┃┗┫┏┫┏┫╋┃┃╋┃
			      ┗━┻━┻━┻┛┗━┻┻━┛
			•°• Deployed Successfully °•°
		   •• Wait till python images are pushed
	   •• Give build logs in @ExtremePro_Userbot if build fails
"
