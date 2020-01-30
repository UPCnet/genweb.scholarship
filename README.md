# genweb.scholarship

## /api/scholarships

Get all scholarships in site by calling: https://vvv/api/scholarships?page=z

```json
{
  "items": [
    {
      "absolute_url": "/xxx/yyy/zzz",
      "description": "Aquest ajut s'adre\u00e7a als estudiants de la UPC que fan una estada de mobilitat per cursar cr\u00e8dits en una de les universitats dels pa\u00efsos que participen en el programa Erasmus+.",
      "end_date": "30/10/2020",
      "id": "ajut-erasmus",
      "path": "http://localhost/xxx",
      "scholarship_type": "Estudis",
      "start_date": "31/07/2020",
      "title": "Ajut Erasmus+"
    },
    {
      "absolute_url": "/xxx/ccc/ggg",
      "description": "Descripci\u00f3 beca",
      "end_date": "25/06/2020",
      "id": "beca-de-prova",
      "path": "http://localhost/xxx",
      "scholarship_type": "Mobilitat",
      "start_date": "11/03/2020",
      "title": "Beca de prova"
    }
  ],
  "more_items": false,
  "total": 2
}
```

## /api/scholarships/{sch_id}?absolute_url=www

Get one scholarship by calling: https://vvv/api/scholarships/{sch_id}?absolute_url=www

```json
{
  "absolute_url": "/xxx/yyy/zzz",
  "academic": "",
  "additional_amount": "",
  "allegations": "<p>Al\u00b7legacions</p>",
  "amount": "",
  "award_date": "10/05/2020",
  "award_resolution": "<p>Publicaci\u00f3 de la resoluci\u00f3 de l\u2019adjudicaci\u00f3</p>",
  "beneficiaries": "<p>Obligacions dels beneficiaris</p>",
  "criteria": "<p>Criteris d\u2019adjudicaci\u00f3</p>",
  "description": "Descripci\u00f3 beca",
  "documentation": "",
  "duration": "<p>Durada de l\u2019ajut</p>",
  "economic": "",
  "end_date": "25/06/2020",
  "general": "",
  "id": "beca-de-prova",
  "incompatibilities": "",
  "organism": "<p>asdfasdfsdf</p>",
  "others": "",
  "path": "http://localhost/xxx",
  "payment": "<p>Pagament</p>",
  "recipients": "<p>dsfasfasdff</p>",
  "regulations": "<p>Normatives</p>",
  "scholarship_type": "Mobilitat",
  "start_date": "11/03/2020",
  "submission": "",
  "title": "Beca de prova"
}

```
