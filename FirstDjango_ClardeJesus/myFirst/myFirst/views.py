from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

def mission(request):
    return HttpResponse('<h1 style="color:maroon;"> CCMS Mission </h1>'
    '<p>The College of Computing and Multimedia Studies shall produce competent and innovative<br>professionals or Technopreneurs in the Information and Communication Technology (ICT)<br>industry adequately prepared in the practice of their profession supportive of national<br>development goals and standards of global excellence.</p>')

def vision(request):
    return HttpResponse('<h1 style="color:maroon;"> CCMS Vision </h1>'
    '<p>The College of Computing and Multimedia Studies shall be a center of excellence in<br>delivering Computing and Multimedia education.</p>')

def objectives(request):
    return HttpResponse('<h1 style="color:maroon;"> CCMS Objectives </h1>'
    '<p>After graduation, alumni of MSEUF-CCS programs shall:<br><br>1. Be employed and demonstrate professionalism, competence<br>and passion in solving contemporary computing problems by<br>developing or utilizing innovative IT solutions;<br><br>2. Embark in lifelong learning or research to attune to the<br>continuous innovation in the IT industry in order to adapt to<br>the changing demands of the globalmarket; and<br><br>3. Exhibit leadership and teamwork, and commitment to their<br>respective local or global organizations.</p>')
