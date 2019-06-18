# crypto-experiments
> Some scripts experimenting with cryptograpy  
>- Ceasar cypher
>- Primefactor
>- En- / Decrypt filer (Fernet)

## Scripts

### ROT.groovy
> Tries all possible rotations (Ceasar cypher)

#### Usage

``` bash
groovy ROT.groovy "CRYPTED"
```
***
### RSACracker.groovy
> Find the largest primefactor (tested with 32 Bit RSA Keys

#### Usage

1. Generate RSA Private Key  
```openssl genrsa -out rsa_32_priv.pem 32```
2. Create RSA Public Key  
```openssl rsa -pubout -in rsa_32_priv.pem -out rsa_32_pub.pem```
3. Get Public Key information  
```openssl rsa -pubin -in rsa_32_pub.pem -text```
```
Public-Key: (32 bit)
Modulus: 2635491359 (0x9d16681f)
Exponent: 65537 (0x10001)
writing RSA key
-----BEGIN PUBLIC KEY-----
MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFAJ0WaB8CAwEAAQ==
-----END PUBLIC KEY-----
```
4. Run the RSACracker.groovy script  passing the Modulus as argument
```groovy RSACracker.groovy 2635491359```
```
Min: 10000 Max: 100000 Possibilities: 90000
effective time:	6.167 sconds
q1: 53267 q2: 49477
```
5. Check the Result with the Private Key **prime1 & prime2 have to match p1 & q2**  
```openssl rsa -text -in rsa_32_priv.pem```
```
Private-Key: (32 bit)
modulus: 2635491359 (0x9d16681f)
publicExponent: 65537 (0x10001)
privateExponent: 994247273 (0x3b430269)
prime1: 53267 (0xd013)
prime2: 49477 (0xc145)
exponent1: 37383 (0x9207)
exponent2: 27053 (0x69ad)
coefficient: 39114 (0x98ca)
writing RSA key
-----BEGIN RSA PRIVATE KEY-----
MC0CAQACBQCdFmgfAgMBAAECBDtDAmkCAwDQEwIDAMFFAgMAkgcCAmmtAgMAmMo=
-----END RSA PRIVATE KEY-----
```
***
### LooneyCrypt.py
> can crypt and decrypt files recursivly using ``Fernet``

#### usage
``` bash
USAGE: python LooneyCrypt.py
	-e root_dir_to_encrypt key : encrypt files recursive
	-d root_dir_to_decrypt key : decrypt files recursive
	-k                         : generates a new key
```
***