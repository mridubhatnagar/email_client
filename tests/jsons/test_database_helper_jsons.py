payload_1 = {
    "partId": "",
    "mimeType": "text/plain",
    "filename": "",
    "headers": [
      {
        "name": "Delivered-To",
        "value": "mridubhatnagar4@gmail.com"
      },
      {
        "name": "Received",
        "value": "by 2002:a59:c329:0:b0:453:b645:4e57 with SMTP id l9csp84151vqp;        Thu, 11 Apr 2024 11:10:16 -0700 (PDT)"
      },
      {
        "name": "X-Google-Smtp-Source",
        "value": "AGHT+IENpVYJ4os6PHHLFdWopp02l5E0ITuE4l13dQiXmC4aP3Htxz2BpuzlAMbkO/R41agFe51W"
      },
      {
        "name": "X-Received",
        "value": "by 2002:a05:6102:21db:b0:479:c133:a743 with SMTP id r27-20020a05610221db00b00479c133a743mr2660488vsg.9.1712859015847;        Thu, 11 Apr 2024 11:10:15 -0700 (PDT)"
      },
      {
        "name": "ARC-Seal",
        "value": "i=1; a=rsa-sha256; t=1712859015; cv=none;        d=google.com; s=arc-20160816;        b=Y2Vq9e/c6XjO4RfOMLcLaqjA6a6FSCu9/N0gDeNJqu54JybqNodQoGxEGt12ffqoIM         S4bs0OW+KSlNyXwhDeQcR+CYLmxcx2XroPRs0LT4/MQWOg89wR5OZj63ZW5e1NEXVVQ/         EpV3cVp+AC6UdQV4CWmvdpJUfvrDrrEOW8gfjwO2vF2/ewZTJtSXLxPt/AJicjdgoaWV         AylTSHFAANEOyWhmyt/WwdiwM5TAzvQ3YxvfHGsOJsT6AEkp59F9vDCysyUhgwswtxu8         5Q/I+tHw+BIQU9Aeh1gVIqh7jV7NHVswZeZoQ/H/lW9yTN9/i7j/DvbQCosEkz9ruTSb         NXXQ=="
      },
      {
        "name": "ARC-Message-Signature",
        "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=to:list-unsubscribe:feedback-id:precedence:subject:message-id         :mime-version:from:date:dkim-signature:dkim-signature;        bh=QqQ9I8i/d0ZnzIQdEhK7ZRQlQRG9aT/g1wgTscUw5n8=;        fh=xzN5ddmY38Eihs5vsFUflhot1UA/4uzNvuSSfdLugYk=;        b=qiCW+Gh6+MxW0jPneTqzMQhGt7sLlOgPJV66cUv9tZM91+O1tRm+alxH/LV6xN3tif         2JpEcd/WV9RHG9NG3Xfk+ZjTLdB8IkriPVN7ftJt97gRUW8euy/KATMSyGXKF+WGvBnr         8CEKp9vA4RjrUgBbpFy5kOUoNAvnKp5NusF5gJIab680vz9/WwH9h0uSwqTqy7nO41eu         vP54AYRRSt4O5FuIQfjpPug6Lw80oxn8JvSIXcQBY7A3DcKvnSwN12jHe0JYyMxmC14v         hFPvnQo/qp3JVJmZLuuf2oUJGRhOYOlylxT28K7h6MNRVjD0RlvFMZnxuwtz1E6XvvCf         6Esw==;        dara=google.com"
      },
      {
        "name": "ARC-Authentication-Results",
        "value": "i=1; mx.google.com;       dkim=pass header.i=@jamesclear.com header.s=cka header.b=f9F7H1Gv;       dkim=pass header.i=@sendgrid.info header.s=smtpapi header.b=XmJB69IA;       spf=pass (google.com: domain of bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com designates 167.89.80.227 as permitted sender) smtp.mailfrom=\"bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com\";       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=jamesclear.com"
      },
      {
        "name": "Return-Path",
        "value": "<bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com>"
      },
      {
        "name": "Received",
        "value": "from o1.ck.h.convertkit.com (o1.ck.h.convertkit.com. [167.89.80.227])        by mx.google.com with ESMTPS id i7-20020a05610220c700b0047a18c287bcsi320016vsr.294.2024.04.11.11.10.15        for <mridubhatnagar4@gmail.com>        (version=TLS1_3 cipher=TLS_AES_128_GCM_SHA256 bits=128/128);        Thu, 11 Apr 2024 11:10:15 -0700 (PDT)"
      },
      {
        "name": "Received-SPF",
        "value": "pass (google.com: domain of bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com designates 167.89.80.227 as permitted sender) client-ip=167.89.80.227;"
      },
      {
        "name": "Authentication-Results",
        "value": "mx.google.com;       dkim=pass header.i=@jamesclear.com header.s=cka header.b=f9F7H1Gv;       dkim=pass header.i=@sendgrid.info header.s=smtpapi header.b=XmJB69IA;       spf=pass (google.com: domain of bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com designates 167.89.80.227 as permitted sender) smtp.mailfrom=\"bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com\";       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=jamesclear.com"
      },
      {
        "name": "DKIM-Signature",
        "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=jamesclear.com; h=content-type:from:mime-version:subject:list-unsubscribe:x-feedback-id: to:cc:content-type:from:subject:to; s=cka; bh=QqQ9I8i/d0ZnzIQdEhK7ZRQlQRG9aT/g1wgTscUw5n8=; b=f9F7H1Gv5lXaDYtCdxytEvROWZYWWpdtOdeAdVZxxOSnaRnraFmBJPMUt0W4vxRjehjx icvEpl2NEx2E52wO1K3Pkooj2nYbBbnGo/PatA8utAMAODD4rUWJPe6YrcnlpBUkv4Rv3t 4XnOLc42gzoCDkMHEvxVa06p9rvUsjO2M="
      },
      {
        "name": "DKIM-Signature",
        "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=sendgrid.info; h=content-type:from:mime-version:subject:list-unsubscribe:x-feedback-id: to:cc:content-type:from:subject:to; s=smtpapi; bh=QqQ9I8i/d0ZnzIQdEhK7ZRQlQRG9aT/g1wgTscUw5n8=; b=XmJB69IAgoBUEV8sQTYlW3Y6Xezg6Ha5BMBYzHlN7vPLJKq3c13wS4dOoKIDO2unDZxH UZ6VbJzgpvMmB+LLdlHS93ey6O/jQwEywAzmzVTUouupw7t9SmPJHQOHvGJmujY3g7Ikpw rJeRg0HCOqvfRB8CAm4qWb49OB2+kQjxU="
      },
      {
        "name": "Received",
        "value": "by filterdrecv-76d8f49b7d-69cps with SMTP id filterdrecv-76d8f49b7d-69cps-1-66182786-2C0        2024-04-11 18:10:14.726779698 +0000 UTC m=+238372.291636982"
      },
      {
        "name": "Received",
        "value": "from ODY3OTg2Mg (unknown) by geopod-ismtpd-28 (SG) with HTTP id s0XRu-ZATXCJcZu6Kwr8SQ Thu, 11 Apr 2024 18:10:14.642 +0000 (UTC)"
      },
      {
        "name": "Content-Type",
        "value": "multipart/alternative; boundary=608e1fa726477b855bd4080d9e1619cecb0cb0b86556d281f6d9406ef967"
      },
      {
        "name": "Date",
        "value": "Thu, 11 Apr 2024 18:10:15 +0000 (UTC)"
      },
      {
        "name": "From",
        "value": "test@gmail.com"
      },
      {
        "name": "Mime-Version",
        "value": "1.0"
      },
      {
        "name": "Message-ID",
        "value": "<d0u43l9qq3h0h4n3lvghncmvxoq44@convertkit-mail4.com>"
      },
      {
        "name": "Subject",
        "value": "3-2-1: What top performers do, and how to deal with critics and detractors"
      },
      {
        "name": "Precedence",
        "value": "bulk"
      },
      {
        "name": "Feedback-ID",
        "value": "13600289:514:broadcast:CK"
      },
      {
        "name": "List-Unsubscribe",
        "value": "<https://unsubscribe.convertkit-mail4.com/d0u43l9qq3h0h4n3lvghncmvxoq44>"
      },
      {
        "name": "X-Report-Spam",
        "value": "<abuse@convertkit.com>"
      },
      {
        "name": "X-Report-Abuse",
        "value": "<abuse@convertkit.com>"
      },
      {
        "name": "X-Feedback-ID",
        "value": "8679862:SG"
      },
      {
        "name": "X-SG-EID",
        "value": "u001.uwZeCzcbUmyUW6ISnVgAafWjQ3UbJyknxu5TaW6ADURKXeOHSJd4eYXEDP9uJfScJzzmGqqFk/9j4v0AC9ecxhFrPknABOLbITW+BQA1tm5yKnCS7cUJodW8rY6IEqukZ/tmIznZqktUZp3KVxf1MhKCebG8WPoHRqJc6uZPLmHFFUeFs+soSkOwQu7fLwZ8R3IG4UlYDXgp6ZAl0C3E42cqBwJ60MsTlb4I2G5evpuDTMxyH7ehCSeNkrABi64z"
      },
      {
        "name": "X-SG-ID",
        "value": "u001.SdBcvi+Evd/bQef8eZF3BpTL9BgbK5wfSJMJGMsmprBTLquV1ImzFIrgTSaJ3+RZKRMcvLAjCcsCrxm/LAgB0nODTzJGOxa0zAJfhsq2CL1BwkWTd+t2t36Xg6N9c7o4WBcEow8ty2FjH4TQi0XxmTJ7IUVmzYPJn538bZqfXmmPtJfIMT6Ce12Abs+Wp80NTI1mPxEpjb5ii06zHqv1zOohBAFJdruwklG5SUg0o3ieWKM2afA/ONXZEMOyMDAYX1avTA8E7ozR+RO8T+S2y8QHIwWtXlszvxU+VuZnXNFLmqJvS+E+hj0Ote1C9ldt3KM4xhJYTV3zy2PrYErNDj8MJzs+BT+EUTWdMIH3unfw9Ff2cE82cOOUCTejsCsaq4BdPOPWpYIufPOxpSg6S3/9UQ5bR3Zpd6oh1jiA7s8="
      },
      {
        "name": "To",
        "value": "testuser@gmail.com"
      },
      {
        "name": "X-Entity-ID",
        "value": "u001.10ccX0iRADaBqPMRJXn8uA=="
      }
    ],
    "body": {
      "size": "0",
      "data": "VGhpcyBpcyB0ZXN0IGVtYWls"
    }
  }

payload_2 = {
    "partId": "",
    "mimeType": "text/plain",
    "filename": "",
    "headers": [
      {
        "name": "Delivered-To",
        "value": "mridubhatnagar4@gmail.com"
      },
      {
        "name": "Received",
        "value": "by 2002:a59:c329:0:b0:453:b645:4e57 with SMTP id l9csp84151vqp;        Thu, 11 Apr 2024 11:10:16 -0700 (PDT)"
      },
      {
        "name": "X-Google-Smtp-Source",
        "value": "AGHT+IENpVYJ4os6PHHLFdWopp02l5E0ITuE4l13dQiXmC4aP3Htxz2BpuzlAMbkO/R41agFe51W"
      },
      {
        "name": "X-Received",
        "value": "by 2002:a05:6102:21db:b0:479:c133:a743 with SMTP id r27-20020a05610221db00b00479c133a743mr2660488vsg.9.1712859015847;        Thu, 11 Apr 2024 11:10:15 -0700 (PDT)"
      },
      {
        "name": "ARC-Seal",
        "value": "i=1; a=rsa-sha256; t=1712859015; cv=none;        d=google.com; s=arc-20160816;        b=Y2Vq9e/c6XjO4RfOMLcLaqjA6a6FSCu9/N0gDeNJqu54JybqNodQoGxEGt12ffqoIM         S4bs0OW+KSlNyXwhDeQcR+CYLmxcx2XroPRs0LT4/MQWOg89wR5OZj63ZW5e1NEXVVQ/         EpV3cVp+AC6UdQV4CWmvdpJUfvrDrrEOW8gfjwO2vF2/ewZTJtSXLxPt/AJicjdgoaWV         AylTSHFAANEOyWhmyt/WwdiwM5TAzvQ3YxvfHGsOJsT6AEkp59F9vDCysyUhgwswtxu8         5Q/I+tHw+BIQU9Aeh1gVIqh7jV7NHVswZeZoQ/H/lW9yTN9/i7j/DvbQCosEkz9ruTSb         NXXQ=="
      },
      {
        "name": "ARC-Message-Signature",
        "value": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;        h=to:list-unsubscribe:feedback-id:precedence:subject:message-id         :mime-version:from:date:dkim-signature:dkim-signature;        bh=QqQ9I8i/d0ZnzIQdEhK7ZRQlQRG9aT/g1wgTscUw5n8=;        fh=xzN5ddmY38Eihs5vsFUflhot1UA/4uzNvuSSfdLugYk=;        b=qiCW+Gh6+MxW0jPneTqzMQhGt7sLlOgPJV66cUv9tZM91+O1tRm+alxH/LV6xN3tif         2JpEcd/WV9RHG9NG3Xfk+ZjTLdB8IkriPVN7ftJt97gRUW8euy/KATMSyGXKF+WGvBnr         8CEKp9vA4RjrUgBbpFy5kOUoNAvnKp5NusF5gJIab680vz9/WwH9h0uSwqTqy7nO41eu         vP54AYRRSt4O5FuIQfjpPug6Lw80oxn8JvSIXcQBY7A3DcKvnSwN12jHe0JYyMxmC14v         hFPvnQo/qp3JVJmZLuuf2oUJGRhOYOlylxT28K7h6MNRVjD0RlvFMZnxuwtz1E6XvvCf         6Esw==;        dara=google.com"
      },
      {
        "name": "ARC-Authentication-Results",
        "value": "i=1; mx.google.com;       dkim=pass header.i=@jamesclear.com header.s=cka header.b=f9F7H1Gv;       dkim=pass header.i=@sendgrid.info header.s=smtpapi header.b=XmJB69IA;       spf=pass (google.com: domain of bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com designates 167.89.80.227 as permitted sender) smtp.mailfrom=\"bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com\";       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=jamesclear.com"
      },
      {
        "name": "Return-Path",
        "value": "<bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com>"
      },
      {
        "name": "Received",
        "value": "from o1.ck.h.convertkit.com (o1.ck.h.convertkit.com. [167.89.80.227])        by mx.google.com with ESMTPS id i7-20020a05610220c700b0047a18c287bcsi320016vsr.294.2024.04.11.11.10.15        for <mridubhatnagar4@gmail.com>        (version=TLS1_3 cipher=TLS_AES_128_GCM_SHA256 bits=128/128);        Thu, 11 Apr 2024 11:10:15 -0700 (PDT)"
      },
      {
        "name": "Received-SPF",
        "value": "pass (google.com: domain of bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com designates 167.89.80.227 as permitted sender) client-ip=167.89.80.227;"
      },
      {
        "name": "Authentication-Results",
        "value": "mx.google.com;       dkim=pass header.i=@jamesclear.com header.s=cka header.b=f9F7H1Gv;       dkim=pass header.i=@sendgrid.info header.s=smtpapi header.b=XmJB69IA;       spf=pass (google.com: domain of bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com designates 167.89.80.227 as permitted sender) smtp.mailfrom=\"bounces+8679862-2158-mridubhatnagar4=gmail.com@ckespa.jamesclear.com\";       dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=jamesclear.com"
      },
      {
        "name": "DKIM-Signature",
        "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=jamesclear.com; h=content-type:from:mime-version:subject:list-unsubscribe:x-feedback-id: to:cc:content-type:from:subject:to; s=cka; bh=QqQ9I8i/d0ZnzIQdEhK7ZRQlQRG9aT/g1wgTscUw5n8=; b=f9F7H1Gv5lXaDYtCdxytEvROWZYWWpdtOdeAdVZxxOSnaRnraFmBJPMUt0W4vxRjehjx icvEpl2NEx2E52wO1K3Pkooj2nYbBbnGo/PatA8utAMAODD4rUWJPe6YrcnlpBUkv4Rv3t 4XnOLc42gzoCDkMHEvxVa06p9rvUsjO2M="
      },
      {
        "name": "DKIM-Signature",
        "value": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=sendgrid.info; h=content-type:from:mime-version:subject:list-unsubscribe:x-feedback-id: to:cc:content-type:from:subject:to; s=smtpapi; bh=QqQ9I8i/d0ZnzIQdEhK7ZRQlQRG9aT/g1wgTscUw5n8=; b=XmJB69IAgoBUEV8sQTYlW3Y6Xezg6Ha5BMBYzHlN7vPLJKq3c13wS4dOoKIDO2unDZxH UZ6VbJzgpvMmB+LLdlHS93ey6O/jQwEywAzmzVTUouupw7t9SmPJHQOHvGJmujY3g7Ikpw rJeRg0HCOqvfRB8CAm4qWb49OB2+kQjxU="
      },
      {
        "name": "Received",
        "value": "by filterdrecv-76d8f49b7d-69cps with SMTP id filterdrecv-76d8f49b7d-69cps-1-66182786-2C0        2024-04-11 18:10:14.726779698 +0000 UTC m=+238372.291636982"
      },
      {
        "name": "Received",
        "value": "from ODY3OTg2Mg (unknown) by geopod-ismtpd-28 (SG) with HTTP id s0XRu-ZATXCJcZu6Kwr8SQ Thu, 11 Apr 2024 18:10:14.642 +0000 (UTC)"
      },
      {
        "name": "Content-Type",
        "value": "multipart/alternative; boundary=608e1fa726477b855bd4080d9e1619cecb0cb0b86556d281f6d9406ef967"
      },
      {
        "name": "Date",
        "value": "Thu, 11 Apr 2024 18:10:15 +0000 (UTC)"
      },
      {
        "name": "From",
        "value": "Test User test@gmail.com"
      },
      {
        "name": "Mime-Version",
        "value": "1.0"
      },
      {
        "name": "Message-ID",
        "value": "<d0u43l9qq3h0h4n3lvghncmvxoq44@convertkit-mail4.com>"
      },
      {
        "name": "Subject",
        "value": "Adventure Awaits!"
      },
      {
        "name": "Precedence",
        "value": "bulk"
      },
      {
        "name": "Feedback-ID",
        "value": "13600289:514:broadcast:CK"
      },
      {
        "name": "List-Unsubscribe",
        "value": "<https://unsubscribe.convertkit-mail4.com/d0u43l9qq3h0h4n3lvghncmvxoq44>"
      },
      {
        "name": "X-Report-Spam",
        "value": "<abuse@convertkit.com>"
      },
      {
        "name": "X-Report-Abuse",
        "value": "<abuse@convertkit.com>"
      },
      {
        "name": "X-Feedback-ID",
        "value": "8679862:SG"
      },
      {
        "name": "X-SG-EID",
        "value": "u001.uwZeCzcbUmyUW6ISnVgAafWjQ3UbJyknxu5TaW6ADURKXeOHSJd4eYXEDP9uJfScJzzmGqqFk/9j4v0AC9ecxhFrPknABOLbITW+BQA1tm5yKnCS7cUJodW8rY6IEqukZ/tmIznZqktUZp3KVxf1MhKCebG8WPoHRqJc6uZPLmHFFUeFs+soSkOwQu7fLwZ8R3IG4UlYDXgp6ZAl0C3E42cqBwJ60MsTlb4I2G5evpuDTMxyH7ehCSeNkrABi64z"
      },
      {
        "name": "X-SG-ID",
        "value": "u001.SdBcvi+Evd/bQef8eZF3BpTL9BgbK5wfSJMJGMsmprBTLquV1ImzFIrgTSaJ3+RZKRMcvLAjCcsCrxm/LAgB0nODTzJGOxa0zAJfhsq2CL1BwkWTd+t2t36Xg6N9c7o4WBcEow8ty2FjH4TQi0XxmTJ7IUVmzYPJn538bZqfXmmPtJfIMT6Ce12Abs+Wp80NTI1mPxEpjb5ii06zHqv1zOohBAFJdruwklG5SUg0o3ieWKM2afA/ONXZEMOyMDAYX1avTA8E7ozR+RO8T+S2y8QHIwWtXlszvxU+VuZnXNFLmqJvS+E+hj0Ote1C9ldt3KM4xhJYTV3zy2PrYErNDj8MJzs+BT+EUTWdMIH3unfw9Ff2cE82cOOUCTejsCsaq4BdPOPWpYIufPOxpSg6S3/9UQ5bR3Zpd6oh1jiA7s8="
      },
      {
        "name": "To",
        "value": "Riya riya@gmail.com"
      },
      {
        "name": "X-Entity-ID",
        "value": "u001.10ccX0iRADaBqPMRJXn8uA=="
      }
    ],
    "body": {
      "size": "0",
      "data": "UGxlYXNlIHJlYWQgdGhlIGluc3RydWN0aW9ucyBjYXJlZnVsbHk="
    }
  }