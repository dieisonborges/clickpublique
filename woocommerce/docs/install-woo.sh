#!/bin/bash

######################################################
# Script de Instalação de Novo Wordpress
# Version: 0.1.0
# By: Dieison
# Date: 05/05/2020
######################################################

USER_INSTALL="dieison"
NAME='wordpress1'
WP_USER='admin_$NAME'
WP_PASS='admin_wordpress1'
DB_USER='$NAME'
DB_PASS='DB@#wordpress1'

#API REST
API_USER_ID="1"
API_DESCRIPTION="clickpublique"
API_PERMISSIONS="read_write"
API_CONSUMER_KEY="fa7070fc1ee2fd38fdfgc38353dfb33ba7fba13033c10e1a520c65a29fdebcb1"
API_CONSUMER_SECRET="cs_d1e016bfd98beadfg3ae83f25f6627bd297129d3"
API_TRUNCATE_KEY="1985dfg"

# Welcome
echo "Install $NAME..."

# Create Wordpress With CLI

# Crie um banco de dados para sua instalação do WordPress:
echo "Create database $NAME"
mysql -e "CREATE DATABASE $NAME;"

# Crie um usuário e senha
echo "Create user $NAME"
mysql -e "CREATE USER '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASS';"

# Configure o nome de usuário e a senha para o banco de dados:
echo "Set Privileges for $NAME"
mysql -e "GRANT ALL PRIVILEGES ON $NAME.* TO '$NAME'@'localhost';"

# Atualize os privilégios 
echo "Reload Privileges"
mysql -e "FLUSH PRIVILEGES;"

# Pasta do servidor web
echo "Open Folder Server"
cd /var/www

# Crie um pasta para o projeto
echo "Create Folder $NAME"
mkdir $NAME

# Definir Permissões
echo "Define Folder Permissions"
chown www-data: $NAME -R
chmod 775 $NAME -R

# Abrir pasta do Projeto
echo "Open Folder Project $NAME"
cd $NAME

# Criar configuração Apache
echo "Set Configuration Apache in sites-available"
echo "
<VirtualHost *:80>

        ServerName $NAME.test

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/$NAME

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
" > /etc/apache2/sites-available/$NAME.conf

#Iniciar arquivo apache
echo "Enable $NAME.conf"
a2ensite $NAME.conf

# Recarregar Apache
echo "Reload Apache"
systemctl reload apache2

# Saindo do root
#echo "Exit root"
#su $USER_INSTALL

# Entrando na pasta do projeto
echo "Open /var/www/$NAME"
cd /var/www/$NAME

# Download da Última Versão do Wordpress
echo "Download Wordpress"
su -c "cd /var/www/$NAME && wp core download" -s /bin/sh $USER_INSTALL

# Adicionar as credenciais do banco de dados MySQL ao WordPress
echo "Configure Core Wordpress"
su -c "wp core config --dbname=$NAME --dbuser=$NAME --dbpass=$DB_PASS --dbhost=localhost --dbprefix=wp_" -s /bin/sh $USER_INSTALL



# Adicione informações adicionais
echo "Configure Aditional Info Wordpress"
su -c "wp core install --url='$NAME.test'  --title='ClickPublique $NAME' --admin_user='$WP_USER' --admin_password='$WP_PASS' --admin_email='admin@$NAME.com'" -s /bin/sh $USER_INSTALL

# Gerando Posts
echo "Post Generator"
su -c "wp post generate --count=10" -s /bin/sh $USER_INSTALL

# Install Woocommerce
echo "Install Woocommerce"
su -c "wp plugin install woocommerce --activate" -s /bin/sh $USER_INSTALL

# Gera Chave REST API
echo "Generate REST API keys"
mysql -e "
USE wordpress1;
INSERT INTO wp_woocommerce_api_keys(user_id, description, permissions, consumer_key, consumer_secret, truncated_key) VALUES ($API_USER_ID, '$API_DESCRIPTION', '$API_PERMISSIONS', '$API_CONSUMER_KEY', '$API_CONSUMER_SECRET', '$API_TRUNCATE_KEY');
"

# Ativar Tema Woocommerce
echo "Activate Woocommerce Theme"
su -c "wp theme install shopay --activate" -s /bin/sh $USER_INSTALL

#Configurar arquvio de host
#nano /etc/hosts

#Adicionar linha
#127.0.0.1       $NAME.test



#FIM
echo "End."
