import numpy as np
import requests
import json
import os
import sys


def execute_workflow_rocket(url_rocket='<YOUR_ROCKET_IP_HERE>/workflows/runWithExecutionContext',wf_id,ip_cookie,cert_path='<YOUR_CRT_FILEPATH_HERE>'):
    
    """
    executes a workflow remotely on Stratio Rocket
    requires the workflow id (wf_id) and rocket url (url_rocket),
    also requires and ip where a cookie for the username can be found (ip_cookie)
    and a .crt certificate for connection
    
    """

    s=requests.Session()


    headers={
        'Content-Type': "application/json",
        'Accept': "application/json"
    }

    req=s.get(ip_cookie) ###url that generates cookie user

    s.cookies['user'] = req.text.split("=")[1]

    data={

      "workflowId": wf_id,
      "executionContext": {
        "extraParams": []

      },
      "projectId": "string"
    }

    
    r = s.post(
        url_rocket,
        headers=headers,
        data=json.dumps(data),
        verify=cert_path
    )

    print(f"[PROCESS] Next Workflow Executed Successfully {r.text}",file=sys.stderr)
    r.close()
    return(200)
