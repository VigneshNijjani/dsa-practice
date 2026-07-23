
const KEY="c90ba277ccfca497e986fc6a74c7e7d8"
const data = async () => {
    try {
        const res = await fetch(`http://api.openweathermap.org/geo/1.0/direct?q=London&limit=5&appid=${KEY}`);
        const result = await res.json();

        // console.log(result);
        for (i=0,i++,i<result.length()){
        console.log(i)
        }

    } catch (error) {
        console.error(error);
    }
};
