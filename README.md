# genweb.scholarship

## /api/scholarships

Get all scholarships in site by calling: https://vvv/api/scholarships

```json
{
  "items": [
    {
      "end_date": "30/10/2020",
      "id": "zzz",
      "path": "http://localhost/xxx/yyy/zzz",
      "scholarship_type": "Estudis",
      "sch_path": "/xxx/yyy/zzz",
      "start_date": "31/07/2020",
      "summary": "Aquest ajut s'adre\u00e7a als estudiants de la UPC que fan una estada de mobilitat per cursar cr\u00e8dits en una de les universitats dels pa\u00efsos que participen en el programa Erasmus+.",
      "title": "Ajut Erasmus+"
    },
    {
      "end_date": "25/06/2020",
      "id": "ggg",
      "path": "http://localhost/xxx/ccc/ggg",
      "scholarship_type": "Mobilitat",
      "sch_path": "/xxx/ccc/ggg",
      "start_date": "11/03/2020",
      "summary": "Descripci\u00f3 beca",
      "title": "Beca de prova"
    }
  ],
  "more_items": false,
  "status": 200,
  "total": 2
}
```

Optional: Get scholarhisps filtered by language: https://vvv/api/scholarships?lang=xx

## /api/scholarships/{sch_id}?absolute_url=www

Get one scholarship by calling: https://vvv/api/scholarships/{sch_id}?sch_path=www

```json
{
  "academic": "",
  "additional_amount": "",
  "allegations": "<p>Al\u00b7legacions</p>",
  "amount": "",
  "award_date": "10/05/2020",
  "award_resolution": "<p>Publicaci\u00f3 de la resoluci\u00f3 de l\u2019adjudicaci\u00f3</p>",
  "beneficiaries": "<p>Obligacions dels beneficiaris</p>",
  "criteria": "<p>Criteris d\u2019adjudicaci\u00f3</p>",
  "documentation": "",
  "duration": "<p>Durada de l\u2019ajut</p>",
  "economic": "",
  "end_date": "25/06/2020",
  "general": "",
  "id": "zzz",
  "incompatibilities": "",
  "organism": "<p>asdfasdfsdf</p>",
  "others": "",
  "path": "http://localhost/xxx/yyy/zzz",
  "payment": "<p>Pagament</p>",
  "recipients": "<p>dsfasfasdff</p>",
  "regulations": "<p>Normatives</p>",
  "scholarship_type": "Mobilitat",
  "sch_path": "/xxx/yyy/zzz",
  "start_date": "11/03/2020",
  "status": 200,
  "submission": "",
  "summary": "Descripci\u00f3 beca",
  "title": "Beca de prova"
}

```
