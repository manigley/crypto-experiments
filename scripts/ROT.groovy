
static void main(String[] args) {

    if (args.size() == 1) {
        String crypted = args[0]; //"YRIRY GJB CNFFJBEQ EBGGRA"
        (1..26).each() { i -> println "Rotation [${i}]:\t - " + rotate(crypted, i) }
    } else {
        println "USAGE: groovy ROT.groovy \"CRYPTED\""
    }
}


List rotate(String crypted, int rotation) {

    // A = 65, Z = 90
    // a = 97, z = 122
    final int MIN_UPPER = 65;
    final int MAX_UPPER = 90;
    final int MIN_LOWER = 97;
    final int MAX_LOWER = 122;

    return Arrays.asList(crypted.split("")).stream()
        .map { i ->
            int ascii = (int)((char) i)  
            if (ascii >= MIN_UPPER && ascii <= MAX_UPPER) {
                if (ascii + rotation > MAX_UPPER) {
                    return (char) (MIN_UPPER -1 + (ascii + rotation) - MAX_UPPER)
                } else {
                    return (char) (ascii + rotation)
                }
            } else if (ascii >= MIN_LOWER && ascii <= MAX_LOWER) {
                if (ascii + rotation > MAX_LOWER) {
                    return (char) (MIN_LOWER - 1 + (ascii + rotation) - MAX_LOWER)
                } else {
                    return (char) (ascii + rotation)
                }
            } else {
                return (char) ascii
            }
        } 
        .collect()
}