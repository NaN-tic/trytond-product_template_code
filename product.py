#This file is part product_template_code module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Template', 'Product']
__metaclass__ = PoolMeta


class Template:
    __name__ = "product.template"
    code = fields.Char('Code', help='Code Product Template')


class Product:
    __name__ = "product.product"

    @classmethod
    def create(cls, vlist):
        pool = Pool()
        Template = pool.get('product.template')

        for vals in vlist:
            if not vals.get('code'):
                template = Template(vals.get('template'))
                if template.code:
                    vals['code'] = template.code
        return super(Product, cls).create(vlist)

    @classmethod
    def write(cls, *args):
        pool = Pool()
        Template = pool.get('product.template')

        actions = iter(args)
        args = []
        templates = []
        for products, values in zip(actions, actions):
            if values.get('code'):
                for product in products:
                    template = product.template
                    if len(template.products) == 1:
                        templates.append({
                            'template': product.template,
                            'code': values.get('code'),
                            })
            args.extend((products, values))

        for t in templates:
            Template.write([t['template']], {'code': t['code']})

        return super(Product, cls).write(*args)
