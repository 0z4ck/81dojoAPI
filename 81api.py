import socket
import hashlib
import re
import time




class 81dojoAPI(object):
    """This class is a wrapper of 81dojo API
    """

    HOST = "shogihub.com";
    PORT = 4081;
    PASS = "";

    def __init__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        s.connect((self.HOST, self.PORT));

    def _handshake(self):
        self.s.send("%%HANDSHAKE\n");
        
    def _login(self, user, passwd, salt):
        digest = hashlib.md5(self.PASS+salt).hexdigest();
        self.s.send("LOGIN  {0} {1} x2 {2}\n".format(user,passwd,digest));

    def _who(self):
        self.s.send("%%WHO\n");
        #message = self.s.recv(1024);
        #who = re.search(r'[#WHO]"(\w{16})"',message).group(1);

    def _list(self):
        self.s.send("%%LIST\n");

    def _gameStart(self,r,u,t,b):
        self.s.send("%%GAME {}_{}-{}-{},{} -\n".format(r,u,t,b,m));
    
    def _fetchOps(self):
        message = self.s.recv(1024);
