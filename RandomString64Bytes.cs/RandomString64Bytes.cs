public static string RandomString64Bytes()
{
string finalString = "";

int i = 0;
while (i <= 8)
{
    string randomString = Path.GetRandomFileName();
    randomString = randomString.Replace(".", "");
    randomString = randomString.Substring(0, 8);

    finalString += randomString;
                
    i += 1;
}
            
return finalString;
}
