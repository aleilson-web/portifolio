import speedtest

teste = speedtest.Speedtest()

# Download

print("Testando download")
velocidade_download = teste.download()

print(f"Velocidade de download:{velocidade_download / 10**6:.2f}")

# Upload

print("Testando upload")
velocidade_upload = teste.upload()

print(f"Velocidade de upload:{velocidade_upload / 10**6:.2f}")

# ping

ping = teste.results.ping
print(f"ping:{ping:.2f}")







