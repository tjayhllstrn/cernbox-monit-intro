"""
Prometheus Simple Function - used to test the Prometheus client library and
see how metrics are scraped through Prometheus.
6/22/2022
"""
from prometheus_client import start_http_server, Summary, Gauge, Counter

#creating metrics
REQUEST_TIME = Summary('request_processing_seconds', 'time spent processing request')
NUMBER_USAGES = Counter('request_number_usages', 'number of increments')
TOTAL_VALUE = Gauge('request_total_value', 'counted value of the program')

@REQUEST_TIME.time()
def counter():
    counter = 0
    while True:
        
        change = input("use comand 'exit' to exit\nincrement counter by: ")
        NUMBER_USAGES.inc()

        if change != "exit":
            change = int(change)
            TOTAL_VALUE.inc(change)
            counter += change
            
        elif change == "exit":
            return print("final total was: ", counter)
            
       
    

if __name__ == "__main__":
    start_http_server(8000)
    counter()
