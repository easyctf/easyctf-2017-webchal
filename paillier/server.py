import SocketServer
import os
import re
import time
import traceback
import logging
from math import sin, cos, pi, sqrt, atan

p = 8144194198641127053467521063088973929365485175581336279930490759203400725623086153929294542350943040473375790841894343662879542882143670576484983482676929
q = 9349990237178389195581522619084514015305492951423232071317276234453300521753669715890246992825146527366147991960266180184131002960074501683578205688324193
n = p * q
l = (p - 1) * (q - 1)
g = n + 1
mu = 50461441817124067084598541006218828107720370909059246792962232658242869571003990015294541684702084151173329882441771747115542549562899610400402036968340066285127945127930744036805832623326255171902722383305695091973581469008587730106329093915495096858331002656658189454919392650001488548518482449865519307486


class RequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:
            self.request.sendall("Enter a message to encrypt (int): ")
            m = int(self.request.recv(1024).strip())
            
            self.request.sendall("Enter r (int): ")
            r = int(self.request.recv(1024).strip())
            if m > 100000000000000000 or m < 0:
                self.request.sendall(
                    'Bad m. We only take m from 0 to 100000000000000000.')
                return
            if r > 100000000000000000 or r < 0:
                self.request.sendall(
                    'Bad r. We only take r from 0 to 100000000000000000.')
                return
            c = (pow(g, m, n**2) * pow(r, n, n**2)) % (n**2)
            self.request.sendall('c: ' + str(c))
        except:
            logging.error(traceback.format_exc())
            return


if __name__ == "__main__":
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8570"))
    server = SocketServer.TCPServer((HOST, PORT), RequestHandler)
    print "Listening on %s:%s" % (HOST, PORT)
    server.serve_forever()
