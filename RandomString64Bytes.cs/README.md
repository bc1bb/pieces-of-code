## Random String 64 Bytes

This function will return a random 64 Bytes string useful for pings (example usage):

```csharp
        static bool PingBool(string address)
        {
            bool result;
            Ping ping = new Ping();

            try
            {
                string data = RandomString64Bytes();
                byte[] buffer = Encoding.ASCII.GetBytes(data);
                int timeout = 50;
                PingOptions options = new PingOptions(128, true);
                
                PingReply rep = ping.Send(address, timeout, buffer, options);
                result = rep.Status == IPStatus.Success;
            }
            catch (PingException)
            {
                result = true;
            }
            finally
            {
                ping.Dispose();
            }

            return result;
        }
```
