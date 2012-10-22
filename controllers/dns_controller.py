from base import app, asJSON, Messages
from service.dnshandler import DNSHandler
from base.security import withPassword
from flask import request

class DNSController:

    @app.route("/dns/list", methods=['GET', 'POST'])
    @withPassword
    def list():
        data = {}
        dns = DNSHandler()
        data["zones"] = dns.getAllEntries()
        if len(data["zones"]) > 0:
            data["success"] = True
        return asJSON(data)
        
    @app.route("/dns/add", methods=['GET', 'POST'])
    @withPassword
    def add():
        data = {}
        msgs = Messages()
        if not request.values.has_key('host'):
            msgs.add(u"no host address supplied")
            data["errors"] = msgs
            return asJSON(data)
        host = request.values['host']
        if not request.values.has_key('name'):
            msgs.add(u"no name supplied")
            data["errors"] = msgs
            return asJSON(data)
        name = request.values['name']
        if not len(msgs.getAll()) > 0:
            dns = DNSHandler()
            data = dns.add(name, host)
        else:
            data["errors"] = msgs
        if data.has_key("error") or data.has_key("errors"):
            data["success"] = False
        return asJSON(data)
        
    @app.route("/dns/editName", methods=['GET', 'POST'])
    @withPassword
    def editName():
        data = {}
        msgs = Messages()
        if not request.values.has_key('from'):
            msgs.add(u"no from name supplied")
            data["errors"] = msgs
            return asJSON(data)
        fromName = request.values['from']
        if not request.values.has_key('to'):
            msgs.add(u"no name supplied")
            data["errors"] = msgs
            return asJSON(data)
        toName = request.values['to']
        if not len(msgs.getAll()) > 0:
            dns = DNSHandler()
            data = dns.editName(fromName, toName)
        else:
            data["errors"] = msgs
        if data.has_key("error") or data.has_key("errors"):
            data["success"] = False
        return asJSON(data)
        
    @app.route("/dns/editHost", methods=['GET', 'POST'])
    @withPassword
    def editHost():
        data = {}
        msgs = Messages()
        if not request.values.has_key('name'):
            msgs.add(u"no name supplied")
            data["errors"] = msgs
            return asJSON(data)
        if not request.values.has_key('host'):
            msgs.add(u"no host address supplied")
            data["errors"] = msgs
            return asJSON(data)
        name = request.values['name']
        host = request.values['host']
        if not name:
            msgs.add(u"no name supplied")
        if not len(msgs.getAll()) > 0:
            dns = DNSHandler()
            data = dns.editHost(name, host)
        else:
            data["errors"] = msgs
        if data.has_key("error") or data.has_key("errors"):
            data["success"] = False
        return asJSON(data)
        
    @app.route("/dns/delete", methods=['GET', 'POST'])
    @withPassword
    def delete():
        data = {}
        msgs = Messages()
        if not request.values.has_key('name'):
            msgs.add(u"no name supplied")
            data["errors"] = msgs
            return asJSON(data)
        name = request.values['name']
        if not len(msgs.getAll()) > 0:
            dns = DNSHandler()
            data = dns.delete(name)
        else:
            data["errors"] = msgs
        if data.has_key("error") or data.has_key("errors"):
            data["success"] = False
        return asJSON(data)
