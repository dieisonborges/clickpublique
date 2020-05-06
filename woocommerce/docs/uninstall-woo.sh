# Remove Wordpress

NAME='wordpress1'
WP_PASS='admin_wordpress1'
DB_PASS='Pass123@Word'

#Para Remover

# Remova a pasta
echo "Remove folder /var/www/$NAME"
rm -rf /var/www/$NAME

# Remova o Banco
echo "Drop database $NAME"
mysql -e "DROP DATABASE $NAME;"

# Remova o Usuário
echo "Drop user $NAME"
mysql -e "DROP USER '$NAME'@'localhost';"

# Desativar configuração
echo "Disable Config $NAME.conf"
a2dissite $NAME.conf

# Remover configuração
echo "Remove configuration $NAME.conf"
rm -rf /etc/apache2/sites-available/$NAME.conf

#Recarregar APACHE
echo "Reload Apache"
systemctl reload apache2

#FIM
echo "End"