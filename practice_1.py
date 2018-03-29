import base64, struct,codecs
with open(r'D:\ChromeDL\fs.jpg','rb') as f:
    p=f.read(30)

def bmp_info(data):
    s = struct.unpack('<ccIIIIIIHH',data)
    if s[0]==b'B' and s[1]==b'M':
        return {'width':s[6],'height':s[7],'color':s[9]}
    else:
        return s
print(bmp_info(p))