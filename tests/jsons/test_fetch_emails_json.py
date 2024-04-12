multipart_alertnative = {
  "partId": "",
  "mimeType": "multipart/alternative",
  "filename": "",
  "headers": [
    {
      "name": "Delivered-To",
      "value": "mridubhatnagar4@gmail.com"
    },
    {
      "name": "Received",
      "value": "by 2002:a59:c329:0:b0:453:b645:4e57 with SMTP id l9csp497807vqp;        Fri, 12 Apr 2024 05:34:52 -0700 (PDT)"
    },
    {
      "name": "X-Google-Smtp-Source",
      "value": "AGHT+IHBoHV8pxG9YpX4lM4btVS/QVktxlberyzP8kpIPxNAREjEu2gjcm3tsEt8NGoV7uUXas/a"
    },
    {
      "name": "X-Received",
      "value": "by 2002:a05:6a00:4642:b0:6ee:1c9d:b471 with SMTP id kp2-20020a056a00464200b006ee1c9db471mr2899443pfb.25.1712925292607;        Fri, 12 Apr 2024 05:34:52 -0700 (PDT)"
    },
    {
      "name": "ARC-Seal",
      "value": "i=1; a=rsa-sha256; t=1712925292; cv=none;        d=google.com; s=arc-20160816;        b=MYN7cGRHgVbwZR8SLdhk3jzsWkivkslUJwpLpX2spxtasn0ldXFn79jHx1AYi0NrKb         rwWNq5+mgOflVu9ZTeZidWFb7m/gOIGUJBGiP84+PFX/qVP22PzM/bUN60Yy9golpuvl         H2eohfpIOLnMMgrGUDaL784KlkDGFhGKqpRR+XyuxTG8H3hMlCazygt3mAAEZ4ort4/X         mm3/CSMl5Swqs+HUHd92fFYpGlD+1kblF+6rItExFO5UP0DuIuzO8b4EPu3un+DkqVr1         lkWrSaO9nh2Kios8xwSM+Rn+xPzdKZLXgwrwsEt47KlFSIltfIr3GbkL3ku7Pl5RhVfh         5rAA=="
    },
    {
      "name": "ARC-Message-Signature",
      "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=list-unsubscribe:message-id:mime-version:reply-to:to:date:subject         :from:dkim-signature;        bh=+IxYagNBbnWtYfH5SJxOOex/XB80L56rQUaCXiQvwvo=;        fh=vVzYstoE+jUoc+8hnVOQ+ZdUFFlEZ52/PG/AbtwcNvE=;        b=Mx4qCGSzrGBeB/rteqQOBtiR4R9AR/3LH13q4nMJN2BCjDtcEtdpGLpwp34ZqYZoNE         KeIRKMNWiGMqQNeAkK3ePTP8POFgsyiOKb/XZJHGNt7pXg6D1gsgwbIoU81nkK/ptPLF         nm2oXHrPeoAh/pq1ma+EhHWrvit4l53saMGWMX3uosRx9ElUqFgY/Lj8/47G+Wrbu5s9         W2xeCTkodn8eAixHMl2gtrztia1AFIW5TDvm+oQKkIWuxJWb856Tioiotx52N3tEeCCb         MGtKJMYPccKbqh0J9LVNzOA4kvZwT2XS21Yd+bjxyJ1R187HgGoaaeVVCB6rmoctZWjZ         wXuw==;        dara=google.com"
    },
    {
      "name": "ARC-Authentication-Results",
      "value": "i=1; mx.google.com;       dkim=pass header.i=@marketing.goindigo.in header.s=neolane header.b=\"GysldLK/\";       spf=pass (google.com: domain of interglobe@marketing.goindigo.in designates 208.67.42.229 as permitted sender) smtp.mailfrom=interglobe@marketing.goindigo.in;       dmarc=pass (p=QUARANTINE sp=REJECT dis=NONE) header.from=marketing.goindigo.in"
    },
    {
      "name": "Return-Path",
      "value": "<interglobe@marketing.goindigo.in>"
    },
    {
      "name": "Received",
      "value": "from r229.marketing.goindigo.in (r229.marketing.goindigo.in. [208.67.42.229])        by mx.google.com with ESMTPS id h5-20020a056a00170500b006eacbf31752si3392718pfc.184.2024.04.12.05.34.51        for <mridubhatnagar4@gmail.com>        (version=TLS1_2 cipher=ECDHE-ECDSA-AES128-GCM-SHA256 bits=128/128);        Fri, 12 Apr 2024 05:34:52 -0700 (PDT)"
    },
    {
      "name": "Received-SPF",
      "value": "pass (google.com: domain of interglobe@marketing.goindigo.in designates 208.67.42.229 as permitted sender) client-ip=208.67.42.229;"
    },
    {
      "name": "Authentication-Results",
      "value": "mx.google.com;       dkim=pass header.i=@marketing.goindigo.in header.s=neolane header.b=\"GysldLK/\";       spf=pass (google.com: domain of interglobe@marketing.goindigo.in designates 208.67.42.229 as permitted sender) smtp.mailfrom=interglobe@marketing.goindigo.in;       dmarc=pass (p=QUARANTINE sp=REJECT dis=NONE) header.from=marketing.goindigo.in"
    },
    {
      "name": "Return-Path",
      "value": "<interglobe@marketing.goindigo.in>"
    },
    {
      "name": "DKIM-Signature",
      "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=marketing.goindigo.in; s=neolane; t=1712925289; bh=+IxYagNBbnWtYfH5SJxOOex/XB80L56rQUaCXiQvwvo=; h=From:Subject:Date:To:MIME-Version:Message-ID:List-Unsubscribe:\t Content-Type; b=GysldLK/Ce4C1kO+A0YFOB8fp6ZtYIr4Yecdyvgk9BiWpR7K/bq+G/ctDDMQWSTQi\t yHsDy5hmcXP2SKXUioxupkVtrvACMGDSFTFc+2lTwZ/E29evTPHuxcZyP1k8D1XOTw\t MQeqzIELFpW0l+Pp6uXUZ9HgYvEe/JghrJ655zCskb+7D4fUQWYbkIRMQYN+wFv/Hz\t VfPqNPUAPtu/JW7fhjCNFzUR+516v4OZBXww0TD16jYEMdDq+BGY1Awdkb/6Ro8Br5\t cqpXNd7jMngFmDThoBzf0w7vCA6sGsxM91tOQ787z8jTL9EdIwYJbrXmySmyasUJuq\t TQlpbLL4TUIkA=="
    },
    {
      "name": "X-MSFBL",
      "value": "+Uk70Iftqh49sC2EcGGr/otsJF9o/AgwrWH3OjyAJDY=|eyJnIjoicHJvZC5kZWZ hdWx0XzRlYmJkYzNjLTFmMmYtNGM2ZS1hNWRhLTg3MjgxYTNiODcxZCIsImIiOiJ hd3NfaW5kaWdvYXZpYXRpb25fcHJvZDJfcHJvZC5kZWZhdWx0X21vbWVudHVtMDR fbXRhMDAyXzIwOC42Ny40Mi4yMjkiLCJyY3B0X21ldGEiOnsgImluIjogImluZGl nb2FfbWlkX3Byb2QyIiwgInIiOiAibXJpZHViaGF0bmFnYXI0QGdtYWlsLmNvbSI sICJtIjogIjE3ODM4OTY1ODYiLCAiZCI6ICIzNDY5Njg2NiIsICJpIjogIiIgfSw iciI6Im1yaWR1YmhhdG5hZ2FyNEBnbWFpbC5jb20ifQ=="
    },
    {
      "name": "Received",
      "value": "from [10.84.255.134] ([10.84.255.134:46281] helo=r230.marketing.goindigo.in) by momentum04.sin2.cpt.adobe.net (envelope-from <interglobe@marketing.goindigo.in>) (ecelerity 4.2.38.999 r(:)) with ESMTP id 67/9D-13234-96A29166; Fri, 12 Apr 2024 05:34:49 -0700"
    },
    {
      "name": "From",
      "value": "IndiGo <mailers@marketing.goindigo.in>"
    },
    {
      "name": "Subject",
      "value": "Claim your Sula offer ☀️"
    },
    {
      "name": "Date",
      "value": "Fri, 12 Apr 2024 20:34:48 +0800"
    },
    {
      "name": "To",
      "value": "<mridubhatnagar4@gmail.com>"
    },
    {
      "name": "Reply-To",
      "value": "IndiGo <no-reply@marketing.goindigo.in>"
    },
    {
      "name": "MIME-Version",
      "value": "1.0"
    },
    {
      "name": "X-mailer",
      "value": "nlserver, Build 6.7.0"
    },
    {
      "name": "Message-ID",
      "value": "<NM6BBE0D68E02116EA2indigoa_mid_prod2@marketing.goindigo.in>"
    },
    {
      "name": "List-Unsubscribe",
      "value": "<mailto:interglobe@marketing.goindigo.in?subject=unsubscribe%3CNM6BBE0D68E02116EA2indigoa_mid_prod2@marketing.goindigo.in%3E>"
    },
    {
      "name": "Content-Type",
      "value": "multipart/alternative; charset=\"windows-1252\"; boundary=\"----=_NextPart_147_457BB812.457BB812\""
    }
  ],
  "body": {
    "size": 0
  },
  "parts": [
    {
      "partId": "1",
      "mimeType": "text/html",
      "filename": "",
      "headers": [
        {
          "name": "Content-Type",
          "value": "text/html; charset=\"utf-8\""
        },
        {
          "name": "Content-Transfer-Encoding",
          "value": "quoted-printable"
        }
      ],
      "body": {
        "size": 19535,
        "data": "PGgxPkhlbGxvIFdvcmxkPC9oMT4="
      }
    }
  ]
}