using Google.Cloud.Firestore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Tez.Controllers
{
    public class HomeController : Controller
    {
        FirestoreDb db;
        [Authorize]
        public ActionResult Index()
        {
            var username = System.Web.HttpContext.Current.User.Identity.Name;
            ViewBag.username = username;
            return View();
        }   
        [Authorize]
        public async System.Threading.Tasks.Task<ActionResult> UserView()
        {
            var username = System.Web.HttpContext.Current.User.Identity.Name;
            db = FirestoreDb.Create("alzheimertakip-e1d1e");
            DocumentReference docRef = db.Collection("Hasta").Document(username);
            DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
            Dictionary<string, object> user = snapshot.ToDictionary();
            ViewBag.username = user["username"];
            return View();
        }

        [Authorize]
        public ActionResult UserNotes()
        {
            var username = System.Web.HttpContext.Current.User.Identity.Name;
            ViewBag.user = username;
            return View();
        }

        public ActionResult Register()
        {
            return View();
        }

        [Authorize]
        public ActionResult DashboardView()
        {
            var username = System.Web.HttpContext.Current.User.Identity.Name;
            ViewBag.username = username;
            return View();
        }

        [Authorize]
        public ActionResult About()
        {
            ViewBag.Message = "Bu proje Yusuf Talha Balıkçın ve Fuat Seven tarafından bitirme projesi olarak yapılmıştır.";

            return View();
        }
        [Authorize]
        public ActionResult Contact()
        {
            ViewBag.Message = "Yusuf Talha Balıkçın ve Fuat Seven";

            return View();
        }
        [Authorize]
        public async System.Threading.Tasks.Task<ActionResult> UserUpdate()
        {
            var username = System.Web.HttpContext.Current.User.Identity.Name;
            db = FirestoreDb.Create("alzheimertakip-e1d1e");
            DocumentReference docRef = db.Collection("Hasta").Document(username);
            DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
            Dictionary<string, object> user = snapshot.ToDictionary();

            ViewData["dict"] = user;
            return View(ViewData);
        }
        [Authorize]
        public async System.Threading.Tasks.Task<ActionResult> SikayetGonder()
        {
            var username = System.Web.HttpContext.Current.User.Identity.Name;
            ViewBag.username = username;
            return View();
        }
        [Authorize]
        public async System.Threading.Tasks.Task<ActionResult> DeleteComplaint(string id, string hastaismi)
        {
            db = FirestoreDb.Create("alzheimertakip-e1d1e");
            DocumentReference cityRef = db.Collection("Complaints").Document(id);
            await cityRef.DeleteAsync();
            return Redirect("/Home/SikayetGonder?hastaismi=" + hastaismi);
        }
    }
}