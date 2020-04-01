# Covid 19 Relief Efforts Data Manager
Data Management system for Covid 19 relief efforts. This is an ongoing development.

## Requirements
- Docker

## Installation (Dev)
1. Create the following; `.env.dev` and `.env-db.dev` refer to the sample `.env` and `.env-db` files.
2. Create a superuser `docker exec web python manage.py createsuperuser` 

## Usage (Dev)
1. Starting a service 
```
bash run_dev.sh
```
2. Stopping a service
```
bash stop_dev.sh
```
3. Open your browser and go to http://localhost:8000/
4. Go to the admin page http://localhost:8000/admin and login to your account.

## Endpoints Summary
1. Organizations
```
http://localhost:8000/organizations/?org_name=<org-name>&page_size=<page-size>&page=<page-number>
```
2. Contact Details
```
http://localhost:8000/contact-details/?org=<org-id>&page_size=<page-size>&page=<page-number>
```
3. Bank Details
```
http://localhost:8000/bank-details/?org=<org-id>&page_size=<page-size>&page=<page-number>
```
4. Other Details
```
http://localhost:8000/other-details/?org=<org-id>&page_size=<page-size>&page=<page-number>
```
5. Address Details
```
http://localhost:8000/address-details/?org=<org-id>&page_size=<page-size>&page=<page-number>
```
6. Pricing Details
```
http://localhost:8000/pricing-details/?org=<org-id>&page_size=<page-size>&page=<page-number>
```
7. Itemized Needs
```
http://localhost:8000/itemized-needs/?org=<org-id>&page_size=<page-size>&page=<page-number>
```

