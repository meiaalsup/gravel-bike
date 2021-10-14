# Gravel Bike Scraper

## SetUp
Export Twilio keys as environment variables:
* `export TWILIO_ACCOUNT_SID=$KEY`
* `export TWILIO_AUTH_TOKEN=$KEY`
* `export MY_PHONE='+18001234567'`

## Run script
run in background forever dump error logs to bike8.out
`nohup python3 gravel-bike.py > bike8.out 2>&1 &`

## Check for process id
`pgrep python3`

