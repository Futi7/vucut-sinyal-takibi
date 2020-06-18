using Google.Cloud.Firestore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;

namespace Tez.Controllers
{
    public class AdminController : Controller
    {
        FirestoreDb db;
        // GET: Admin
        [Authorize]
        public async System.Threading.Tasks.Task<ActionResult> Index()
        {
            var username = System.Web.HttpContext.Current.User.Identity.Name;
            db = FirestoreDb.Create("alzheimertakip-e1d1e");
            DocumentReference docRef = db.Collection("Hasta").Document(username);
            DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
            Dictionary<string, object> user = snapshot.ToDictionary();
            if (user["role"].ToString() == "A")
            {
                ViewBag.username = username;
                return View();
            }
            else
                return Redirect("/Home/Index");
        }
        [Authorize]
        public async System.Threading.Tasks.Task<ActionResult> AdminView(string hastaismi)
        {
            var username = System.Web.HttpContext.Current.User.Identity.Name;
            db = FirestoreDb.Create("alzheimertakip-e1d1e");
            DocumentReference docRef = db.Collection("Hasta").Document(username);
            DocumentSnapshot snapshot = await docRef.GetSnapshotAsync();
            Dictionary<string, object> user = snapshot.ToDictionary();
            if (user["role"].ToString() == "A")
            {
                ViewBag.username = hastaismi;
                return View();
            }
            else
                return Redirect("/Home/Index");
        }
        [Authorize]
        public ActionResult AdminDashboardView(string hastaismi)
        {
            ViewBag.username = hastaismi;
            return View();
        }

        [Authorize]
        public ActionResult SendNote(string hastaismi)
        {
            ViewBag.username = hastaismi;
            return View();
        }
        [Authorize]
        public async System.Threading.Tasks.Task<ActionResult> DeleteNote(string id,string hastaismi)
        {
            db = FirestoreDb.Create("alzheimertakip-e1d1e");
            DocumentReference cityRef = db.Collection("Notes").Document(id);
            await cityRef.DeleteAsync();
            return Redirect("/Admin/SendNote?hastaismi="+hastaismi);
        }
        [Authorize]
        public ActionResult Sikayetler()
        {
            return View();
        }
    }
}