(Invoke-WebRequest -Uri "http://localhost:8000" `
-Method POST `
-Headers @{ "Content-Type" = "application/json" } `
-Body '{ "method": "get_weather", "params": { "location": "Agra" } }'   
).Content