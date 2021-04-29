import mysql.connector as mc

class mysql():
    def __init__(self):
        self.mydb = mc.connect(
            host="localhost",
            user="root",
            password="ElonMusk17",
            auth_plugin='mysql_native_password',
            db='pl_project'
        )
        self.mycursor = self.mydb.cursor()
        self.currencies = {
            "Bitcoin": ('BTC', "2018-05-15"),
            "Ethereum": ('ETH', "2019-04-04"),
            "Ripple's XRP":('XRP', "2018-05-16"),
            "Dash":('DASH','2018-05-16')

        }