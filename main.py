import requests
import statistics
import time
import csv
import json

with open('routes.json', 'r') as file:
    config = json.load(file)

bearer_token = config["bearer_token"]
num_requests = config["num_requests"]
timeout = config["timeout"]
routes = config["routes"]

headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

def test_route(url, method, body):
    response_times = []
    errors = 0

    for _ in range(num_requests):
        start_time = time.time()
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, timeout=timeout)
            elif method == "POST" and body:
                response = requests.post(url, headers=headers, data=json.dumps(body), timeout=timeout)
            else:
                continue

            response_time = (time.time() - start_time) * 1000  # Convertendo para ms
            response_times.append(response_time)
            if response.status_code >= 400:
                errors += 1
        except requests.exceptions.RequestException:
            errors += 1

    return response_times, errors

results = {}
for route, config in routes.items():
    print(f"Testando a rota: {route}")
    times, errors = test_route(config["url"], config["method"], config["body"])
    if times:
        results[route] = {
            "min": round(min(times), 2),
            "max": round(max(times)),
            "mean": round(statistics.mean(times)),
            "std_dev": round((statistics.stdev(times) if len(times) > 1 else 0), 2),
            "p90": round(statistics.quantiles(times, n=10)[8], 2),
            "p95": round(statistics.quantiles(times, n=20)[18], 2),
            "p99": round(statistics.quantiles(times, n=100)[98], 2),
            "errors": errors,
            "total_requests": num_requests
        }
    else:
        results[route] = {
            "errors": errors,
            "total_requests": num_requests
        }

output_file = "response_times.csv"

with open(output_file, mode="w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow([
        "Rota", "Tempo Mínimo (ms)", "Tempo Máximo (ms)", "Tempo Médio (ms)",
        "Desvio Padrão (ms)", "P90 (ms)", "P95 (ms)", "P99 (ms)",
        "Erros", "Total de Requisições"
    ])
    for route, data in results.items():
        writer.writerow([
            route,
            data.get("min", "N/A"),
            data.get("max", "N/A"),
            data.get("mean", "N/A"),
            data.get("std_dev", "N/A"),
            data.get("p90", "N/A"),
            data.get("p95", "N/A"),
            data.get("p99", "N/A"),
            data["errors"],
            data["total_requests"]
        ])

print(f"\nResultados salvos em {output_file}")
