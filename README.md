# API

API DOCS: https://uptimerobot.com/api/

## Problem at hand:

1. Provide the average uptime for the last week <br />
2. Provide the details of the last downtime <br />
3. Calculate the average total uptime across all monitors since the last downtime event <br />

Reference information: <br />
• API key (ur828173-4544bcf8143509466865be09) <br />
• URL to POST (https://api.uptimerobot.com/v2/getMonitors) <br />
• Documentation (https://uptimerobot.com/api/) <br />
• List of monitors (790608131, 784355743, 784355767, 784355758, and 784355759) <br />

## Answers

Calculation for Average uptime for the last week:    [ Weekly downtime periods(in seconds) = 604800 - (Uptime * 604800) ]

Monitor : *131
    Duration : 11951720 (i.e. downtime in seconds)
    