using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(EasyTry.Startup))]
namespace EasyTry
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
