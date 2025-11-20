names=["James","Siva","Joker"]
ages=[24,18,6,1]
//console.log(names);
//module.exports="James";//James
//module.exports=names;//[ 'James', 'Siva', 'Joker' ]

module.exports={
        PersonName:names,
        PersonAge:ages
}
// {
//   PersonName: [ 'James', 'Siva', 'Joker' ],
//   PersonAge: [ 24, 18, 6, 1 ]
// }

module.exports={
    names,
    ages
}       //{ names: [ 'James', 'Siva', 'Joker' ], ages: [ 24, 18, 6, 1 ] }