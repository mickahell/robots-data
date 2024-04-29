# Watchy data

Repository for the data collected by my esp32 watch.

## Steps

To trigger the steps script :

```bash
curl -L -X POST https://api.github.com/repos/mickahell/robots-data/dispatches \
    -H "Accept: application/vnd.github+json" -H "Authorization: token ${TOKEN}" \
    -d '{
        "event_type": "watchy-data",
        "client_payload":
        {
            "data-name":"steps", "date":"01-01-1970", "hour":"00", "data":"7000"
        }
    }'
```
