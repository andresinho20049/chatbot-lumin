from redis import Redis, ConnectionError

# Set up Redis connection
try:
    redis_conn = Redis(host='redis', port=6379, db=0)
except ConnectionError as e:
    print(f"Redis connection error: {e}")
    exit()

def storeData(text):
    # Store text data in Redis vector database
    redis_conn.set("text_vector", text.encode('utf-8'))

def getData():
    try:
        text_vector = redis_conn.get("text_vector")

        if text_vector is None:
            return ''
        
        return text_vector.decode('utf-8')
    except ConnectionError as e:
        print(f"Redis connection error: {e}")
        exit()

def setValueByKey(key, value):
    isSucess = redis_conn.set(key, value.encode('utf-8'))
    if isSucess is None:
        print("Cannot persist value in database")

def getValueByKey(key):
    try:
        result = redis_conn.get(key)

        if result is None:
            return result
        
        return result.decode('utf-8')
    except ConnectionError as e:
        print(f"Redis connection error: {e}")
        exit()