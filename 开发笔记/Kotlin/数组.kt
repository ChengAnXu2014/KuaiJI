创建数组的两种方式：
fun main() {
    var vr1=arrayOf(1,2,3)
    var vr2=Array(5,{i->(i+1)*5})
    for(i in vr2)
        println(i)
}
**********************************
ByteArray     byteArrayOf()
ShortArray    shortArrayOf()
IntArray      intArrayOf()
LongArray     longArrayOf()
FloatArray    floatArrayOf()
DoubleArray   doubleArrayOf()
BooleanArray  booleanArrayOf()
************
fun main() {
    var vr1=intArrayOf(1,2,3,4,5)
    println("IntArray:"+vr1[0])
    var vr2=shortArrayOf(1,2,3,4,5)
    println("ShortArray:"+vr2[1])
    var vr3=byteArrayOf(1,2,3,4,5)
    println("ByteArray:"+vr3[2])
    var vr4= longArrayOf(1,2,3,4,5)
    println("LongArray:"+vr4[3])
    var vr5= doubleArrayOf(1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8)
    println("DoubleArray:"+vr5[4])
    var vr6= floatArrayOf(1f,2f,3f,4f,5f,6f,7f,8f,9f)
    println("FloatArray:"+vr6[5])
    var vr7= booleanArrayOf(false,true,false,true,false,true,false,true,false,true,false,true)
    println("BooleanArray:"+vr7[6])
}