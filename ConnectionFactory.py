import psycopg2


class ConnectionFactory():
    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def createConnection(self, databaseName):
        conn_string = self._createConnString()
        if databaseName:
            databaseTxt = " dbname= %s" % databaseName
            conn_string = conn_string + databaseTxt
        return psycopg2.connect(conn_string)

    def _createConnString(self):
        conn_string = "host=localhost port= {0} user= {1}  password={2}"
        return conn_string.format(self.port, self.user, self.password)
