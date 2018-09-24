using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using ClientRejistration.Models;

namespace ClientRejistration.Controllers
{
    public class ClientController : Controller
    {
        // GET: Client
        public ActionResult AddorEdit(int id =0)
        {
            Client ClientModel = new Client();
            return View(ClientModel);
        }
    }
}