# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone import api
from five import grok

from genweb.scholarship.api import ApiResponse
from genweb.scholarship.api import ObjectNotFound
from genweb.scholarship.api import REST
from genweb.scholarship.api import api_resource
from genweb.scholarship.api.root import APIRoot


class Scholarships(REST):
    """
        /api/scholarships
        and
        /api/scholarships/sch_ID

        Get all Scholarships by "X-Oauth-Username"
    """

    placeholder_type = "scholarship"
    placeholder_id = 'sch_id'

    grok.adapts(APIRoot, IPloneSiteRoot)

    @api_resource(required=[])
    def GET(self):
        results = []
        properties = api.portal.get_tool(name='portal_properties')
        sch_token = properties.scholarship_properties.sch_token
        try:
            lang = self.params['lang']
        except:
            lang = 'ca'
        if self.request.get_header('Token') == sch_token:
            scholarships = api.content.find(
                portal_type="Scholarship",
                review_state=['published'],
                sort_order='descending',
                sort_on='effective',
                Language=lang,
                )
            total = len(scholarships)
            items_x_page = 10  # Default items per page
            pagination_page = self.params.pop('page', None)
            if pagination_page:
                if pagination_page == 'all':
                    more_items = False
                else:
                    if pagination_page == '0':
                        pagination_page = 1
                    start = int(items_x_page) * (int(pagination_page) - 1)
                    end = int(items_x_page) * int(pagination_page)
                    scholarships = scholarships[start:end]
                    more_items = True if end < total else False
            else:
                # Don't page, return first 10 => ?page=1
                scholarships = scholarships[0:items_x_page]
                more_items = True if items_x_page < total else False
            for item in scholarships:
                obj = item.getObject()
                scholarship_type = obj.scholarship_type
                start_date = obj.start_date.strftime("%d/%m/%Y") if obj.start_date else ''
                deadline = obj.deadline.strftime("%d/%m/%Y") if obj.deadline else ''
                sch_path = '/'.join(obj.getPhysicalPath()[3:])
                scholarship = dict(title=item.Title,
                                   id=item.id,
                                   summary=obj.summary.output if obj.summary else '',
                                   path=item.getURL(),
                                   sch_path=sch_path,
                                   scholarship_type=scholarship_type,
                                   start_date=start_date,
                                   end_date=deadline,
                                   )
                results.append(scholarship)
            values = dict(status=200,
                          items=results,
                          more_items=more_items,
                          total=total)
        else:
            values = dict(status=403,
                          items=results,
                          more_items=False,
                          total=0)
        return ApiResponse(values)


class Scholarship(REST):
    """
        /api/scholarships/{sch_id}
    """
    grok.adapts(Scholarships, IPloneSiteRoot)

    def __init__(self, context, request):
        super(Scholarship, self).__init__(context, request)

    # /api/scholarships/{obj_path_id}?sch_path={sch_path}
    @api_resource(required=['sch_id'])
    def GET(self):
        properties = api.portal.get_tool(name='portal_properties')
        sch_token = properties.scholarship_properties.sch_token
        if self.request.get_header('Token') == sch_token:
            root_path = '/'.join(api.portal.get().getPhysicalPath())
            sch_path = self.params['sch_path']
            path = root_path + '/' + sch_path
            items = api.content.find(portal_type="Scholarship",
                                     path=path)
            if items:
                for item in items:
                    obj = item.getObject()
                    summary = obj.summary.output if obj.summary else ''
                    scholarship_type = obj.scholarship_type
                    organism = obj.organism.output if obj.organism else ''
                    recipients = obj.recipients.output if obj.recipients else ''
                    others = obj.others.output if obj.others else ''
                    general = obj.general_requirements.output if obj.general_requirements else ''
                    academic = obj.academic_requirements.output if obj.academic_requirements else ''
                    economic = obj.economic_requirements.output if obj.economic_requirements else ''
                    incompatibilities = obj.incompatibilities.output if obj.incompatibilities else ''
                    start_date = obj.start_date.strftime("%d/%m/%Y") if obj.start_date else ''
                    deadline = obj.deadline.strftime("%d/%m/%Y") if obj.deadline else ''
                    submission = obj.submission.output if obj.submission else ''
                    documentation = obj.documentation.output if obj.documentation else ''
                    amount = obj.amount.output if obj.amount else ''
                    additional_amount = obj.additional_amount.output if obj.additional_amount else ''
                    duration = obj.duration.output if obj.duration else ''
                    payment = obj.payment.output if obj.payment else ''
                    beneficiaries = obj.beneficiaries.output if obj.beneficiaries else ''
                    criteria = obj.criteria.output if obj.criteria else ''
                    award_date = obj.award_date.strftime("%d/%m/%Y") if obj.award_date else ''
                    award_resolution = obj.award_resolution.output if obj.award_resolution else ''
                    allegations = obj.allegations.output if obj.allegations else ''
                    regulations = obj.regulations.output if obj.regulations else ''
                    scholarship = dict(status=200,
                                       title=item.Title,
                                       id=item.id,
                                       summary=summary,
                                       path=item.getURL(),
                                       absolute_url=obj.absolute_url_path(),
                                       organism=organism,
                                       recipients=recipients,
                                       others=others,
                                       general=general,
                                       academic=academic,
                                       economic=economic,
                                       incompatibilities=incompatibilities,
                                       scholarship_type=scholarship_type,
                                       start_date=start_date,
                                       end_date=deadline,
                                       submission=submission,
                                       documentation=documentation,
                                       amount=amount,
                                       additional_amount=additional_amount,
                                       duration=duration,
                                       payment=payment,
                                       beneficiaries=beneficiaries,
                                       criteria=criteria,
                                       award_date=award_date,
                                       award_resolution=award_resolution,
                                       allegations=allegations,
                                       regulations=regulations,
                                       )
            else:
                raise ObjectNotFound('Scholarship not found')
        else:
            scholarship = dict(status=403)
        return ApiResponse(scholarship)
