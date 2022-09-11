#!/bin/bash
# This script downloads covid data and displays it

POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases."

InICUCurrently=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].inIcuCurrently')
TODAY=$(date)

echo "On $TODAY, there were $InICUCurrently patients currently in the ICU for covid."

OnVentilatorCurrently=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].onVentilatorCurrently')
TODAY=$(date)

echo "On $TODAY, there were $OnVentilatorCurrently patients on a ventilator due to covid."

DEATH=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].death')
TODAY=$(date)

echo "On $TODAY, there were $DEATH deaths due to covid."
