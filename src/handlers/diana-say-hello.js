const dynamodb = require('aws-sdk/clients/dynamodb');
const docClient = new dynamodb.DocumentClient();

exports.dianaFunction = async (event, context) => {
    const message = 'Hello from Lambda!';
    // const tableName = process.env.DDB_TABLE;
    // const logStreamName = context.logStreamName;
    // var params = {
    //     TableName : tableName,
    //     Key: { id : logStreamName },
    //     UpdateExpression: 'set invocations = if_not_exists(invocations, :start) + :inc',
    //     ExpressionAttributeValues: {
    //         ':start': 0,
    //         ':inc': 1
    //     },
    //     ReturnValues: 'ALL_NEW'
    // };
    // await docClient.update(params).promise();

    // const response = {
    //     body: JSON.stringify(message)
    // };
    const response = {
        body: JSON.stringify('hello there!')
    };
    console.log(`body: ${response.body}`);
    return response;
}