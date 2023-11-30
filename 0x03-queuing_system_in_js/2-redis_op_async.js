/*eslint-disable no-console */
import redis from "redis";
const util = require("utill");

// create a redis client
const client = redis.createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
});

client.on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
});

client.getAsync = util.promisify(client.get).bind(client)
client.setAsync = util.promisify(client.set).bind(client)


async function setNewSchool(schoolName, value) {
   try {
    const result = await client.setAsync(schoolName, value);
    console.log(`Reply: ${reply}`);
   } catch (error) {
     console.error(err);
   }
}
async function displaySchoolValue(schoolName) {
   try {
    const reply = await client.getAsync(schoolName);
    console.log(reply);
   } catch (err) {
    console.error(err)
   }
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');