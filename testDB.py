from database.DB_connect import get_connection

cnx = get_connection()
print("Connessione:", cnx)

if cnx:
    cur = cnx.cursor()
    cur.execute("SELECT COUNT(*) FROM corso")
    print("Numero corsi:", cur.fetchone()[0])
    cur.close()
    cnx.close()