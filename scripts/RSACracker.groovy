/*
Problem 3
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


generate RSA private key
$ openssl genrsa -out rsa_32_priv.pem 32

create RSA public key
$ openssl rsa -pubout -in rsa_32_priv.pem -out rsa_32_pub.pem

get public key information
$ openssl rsa -pubin -in rsa_32_pub.pem -text

Public-Key: (32 bit)
Modulus: 3690510347 (0xdbf8b80b)
Exponent: 65537 (0x10001)
writing RSA key
-----BEGIN PUBLIC KEY-----
MCAwDQYJKoZIhvcNAQEBBQADDwAwDAIFANv4uAsCAwEAAQ==
-----END PUBLIC KEY-----

run the groovy script
$ groovy RSACracker.groovy 3113019233
Min: 10000 Max: 100000 Possibilities: 90000
effective time:	8.441 sconds
q1: 62497 q2: 59051

check primes with private key
$ openssl rsa -text -in rsa_32_priv.pem

Private-Key: (32 bit)
modulus: 3690510347 (0xdbf8b80b)
publicExponent: 65537 (0x10001)
privateExponent: 2941127873 (0xaf4e0cc1)
prime1: 62497 (0xf421)
prime2: 59051 (0xe6ab)
exponent1: 3617 (0xe21)
exponent2: 24523 (0x5fcb)
coefficient: 21854 (0x555e)
writing RSA key
-----BEGIN RSA PRIVATE KEY-----
MCwCAQACBQDb+LgLAgMBAAECBQCvTgzBAgMA9CECAwDmqwICDiECAl/LAgJVXg==
-----END RSA PRIVATE KEY-----
*/


static void main(String[] args) {

    if (args.size() == 1) {
        printLargestPrimeFactor(Long.valueOf(args[0]))
    } else {
        println "USAGE: groovy RSACracker.groovy \"PUBLIC-KEY-Modulus\""
    }
}

void printLargestPrimeFactor(Long n) {
    Long largestPrimeFactor = 1L
    Long min = Math.pow(10, n.toString().length() / 2) / 10
    Long max = min * 10
    Long possibilities = max - min
    Long start = System.currentTimeMillis()
    println "Modulus: " + n
    println "Min: ${min} Max: ${max} Possibilities: ${possibilities}"
    for (Long i = min; i < max; i++) {
      if (n / i < largestPrimeFactor) {
        println "effective time:\t${(System.currentTimeMillis() - start) / 1000} sconds"
        println "q1: ${largestPrimeFactor} q2: ${n / largestPrimeFactor}"
        break
      }
      if (isPrime(i) && n % i == 0) {
        Long tmp = n / i
        if (tmp > i && isPrime(tmp)) {
            i = tmp
            largestPrimeFactor = i
        }
      }
    }
}

boolean isPrime(Long n) {
  if (n != 2)
    for (i in 2..n/2) {
      if (n % i == 0) {
        return false
      }
    }
  return true
}
