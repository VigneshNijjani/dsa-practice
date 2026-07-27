
const KEY="c90ba277ccfca497e986fc6a74c7e7d8"
city="hyderabad"
const data = async () => {
    try {
        const res = await fetch(`http://api.openweathermap.org/geo/1.0/direct?q=${city}&limit=5&appid=${KEY}`);
        const result = await res.json();

        // console.log(result);
        for (i of result){
            console.log(i.name,i.state,i.country)
        }
        

    } catch (error) {
        console.error(error);
    }
};
data()