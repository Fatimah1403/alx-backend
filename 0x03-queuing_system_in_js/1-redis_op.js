/*eslint-disable no-console */
import redis from "redis";

// create a redis client
const client = redis.createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

client.on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, result) => {
        if (err) {
            console.error(err);
        }
        console.log(`Reply: ${result}`)
    });
}
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, result) => {
        if (err) {
            console.error(err);
        }
        console.log(result)


    });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');


