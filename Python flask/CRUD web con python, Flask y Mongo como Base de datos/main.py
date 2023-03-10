#XDDD#
from website import create_app

app = create_app()

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    
#Aqui podemos definir la ip y el puerto que usaremos, vemos como se hace, el host 0.0.0.0 es local=localhost o 172.0.0.1
# https://www.youtube.com/watch?v=affNd5VpJBQ