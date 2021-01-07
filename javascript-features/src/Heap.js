
// get Heap's algorithms

// function getPermutations(1, 2, 3)
// function getPermutations(A, 1, C, 2, 3)
// generate result "321,312,231,213,132,123"

// output returns numbers without letters, from highest to lowest value




const getPermutations = ( ...arry ) => {

    const convert = (array) => {

        return array[0].split(', ').filter(element => element * 1)

    }

    const output = []
    const swapThePosition = ( arrayToSwap, first, second ) => {
        const positionOfFirst = arrayToSwap[first]
        arrayToSwap[first] = arrayToSwap[second]
        arrayToSwap[second] = positionOfFirst
    }

    const generate = (n, featureArray) => {

        if (n == 1) {
            return output.push(featureArray.slice())
        }

        generate(n - 1, featureArray)

        for (let i = 0; i < n - 1; i++) {
            if (n % 2 == 0) {
                swapThePosition(featureArray, i, n - 1)
            } else {
                swapThePosition(featureArray, 0, n - 1)
            }
            generate(n - 1, featureArray)

        }
        
    }
    
    generate(convert(arry).length, convert(arry).slice())


    const joinValues = output.map(arr => arr.join('') * 1).sort((a, b) => b - a)

    return joinValues.join(',')

}

console.log(getPermutations( '1, A, 2, 3' ))