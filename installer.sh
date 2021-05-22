#pip install . -r requirements.txt

## installing at loc
CATERPATH="~/"
echo "Installing CaterApp in home directory ($HOME)..."
mkdir ~/CaterApp
mv ../CaterApp/* ~/CaterApp/

## setting start command
callAlias="alias cater-app=\"python ~/CaterApp/caterapp/cater.py\""
CATERHEADER="# >>> CaterApp command >>>"
CATERFOOTER="# <<< CaterApp command <<<"

if ls -a ~ | grep -q .bashrc
then
    if ! cat ~/.bashrc | grep -q 'CaterApp command'
    then
        echo  >> ~/.bashrc
        echo $CATERHEADER >> ~/.bashrc
        echo "# !! auto generated alias for CaterApp" >> ~/.bashrc
        echo $callAlias >> ~/.bashrc
        echo "$CATERFOOTER" >> ~/.bashrc
        printf "\n\n" >> ~/.bashrc
        source ~/.bashrc
    fi
else
    echo "bash is not installed"
fi

if ls -a ~ | grep -q .zshrc
then
    if ! cat ~/.zshrc | grep -q 'CaterApp command'
    then
        echo $CATERHEADER >> ~/.zshrc
        echo "# !! auto generated alias for CaterApp" >> ~/.zshrc
        echo $callAlias >> ~/.zshrc
        echo "$CATERFOOTER" >> ~/.zshrc
        printf "\n\n" >> ~/.zshrc
    fi
else
    echo "zsh is not installed"
fi

echo "-------------------"

printf "\nUse 'cater-app' to use the application\n\n"

rm -rf ../CaterApp/